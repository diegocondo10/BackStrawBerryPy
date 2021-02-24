import calendar
import io
import os
from datetime import date

import requests
from django.utils.translation import gettext as _
from docx.shared import Mm
from docxtpl import InlineImage, DocxTemplate

from BackStrawBerryPy.models import BaseModel
from BackStrawBerryPy.settings import BASE_DIR
from apps.Matriculas.models import AlumnoAula
from apps.Notas.models import NotaAlumno, EvidenciaNotaAlumno
from apps.Personas.models import Personal
from utils.functions import create_docx, docx_to_bytes, create_docx_bytes, get_edad, concat_if_exist

DIR_REPORTES = os.path.join(BASE_DIR, 'static', 'reportes')


def get_reporte(reporte):
    return os.path.join(DIR_REPORTES, reporte)


def reporte_nomina():
    personal = Personal.objects.filter(auth_estado=BaseModel.ACTIVO)

    docx = create_docx(
        file=get_reporte('MatrizPersonalIpca.docx'),
        context={
            'personal': [
                dict(
                    index=i + 1,
                    nombres=item.persona.get_nombres_apellidos(),
                    identificacion=item.persona.identificacion,
                    titulo_profecional=item.titulo,
                    celular=item.persona.celular_uno,
                    correo=item.persona.correo,
                    funcion=item.get_funciones_str()
                )
                for i, item in enumerate(personal)
            ]
        }
    )
    file_stream = io.BytesIO()
    docx.save(file_stream)
    file_stream.seek(0)
    return file_stream


def reporte_notas(id_matricula, id_docente, area_trabajo, responsable):
    matricula = AlumnoAula.objects.get(pk=id_matricula)

    notas = NotaAlumno.objects.prefetch_related("evidencias").filter(
        alumno_aula_id=id_matricula,
        auth_estado=BaseModel.ACTIVO
    ).order_by('componente__nombre')

    imgs = EvidenciaNotaAlumno.objects.filter(
        nota_id__in=[nota.pk for nota in notas]
    ).values_list('url', flat=True)

    tpl = DocxTemplate(get_reporte('MATRIZ_INFORME.docx'))
    imgs_objs = dict()

    for index, img in enumerate(list(imgs)):
        response = requests.get(img, stream=True)
        image = io.BytesIO(response.content)
        my_image = InlineImage(tpl, image, width=Mm(150))
        imgs_objs.__setitem__(f'img{index + 1}', my_image)

    tpl.render({**{
        'responsable': responsable,
        'mes': _(calendar.month_name[date.today().month]).upper(),
        'area_de_trabajo': area_trabajo,
        'docente': Personal.objects.select_related('persona').get(pk=id_docente).persona.__str__(),
        'coordinador': matricula.aula.periodo.coordinador.persona.__str__(),
        'director': matricula.aula.periodo.director.persona.__str__(),
        'notas': [
            dict(
                index=i + 1,
                componente=item.componente.nombre,
                actividad=item.titulo,
                resultado=item.resultado,
                observacion=item.observaciones,
            )
            for i, item in enumerate(notas)
        ],
    }, **imgs_objs})
    return docx_to_bytes(tpl)


def reporte_ficha_inscripcion(id_matricula):
    matricula = AlumnoAula.objects \
        .select_related('alumno__persona', 'aula') \
        .get(pk=id_matricula)

    persona = matricula.alumno.persona
    aula = matricula.aula
    alumo = matricula.alumno
    return create_docx_bytes(
        file=get_reporte("FichaInscripcion.docx"),
        context={
            'apellidos': persona.get_apellidos(),
            'nombres': persona.get_nombres(),
            'lugar': persona.direccion_domiciliaria,
            'fecha_n': persona.fecha_nacimiento.strftime('%d/%m/%Y'),
            'edad': get_edad(persona.fecha_nacimiento),
            'cedula': persona.identificacion,
            'conadis': persona.carnet_conadis,
            'nivel_a': aula.grado,
            'promovido': aula.grado,
            'tratamiento': matricula.tratamiento,
            'diagnostico': matricula.diagnostico_clinico,
            'apellidos_p': concat_if_exist(alumo.padre.get('primer_apellido'), alumo.padre.get('segundo_apellido'))
        }
    )
