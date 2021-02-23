import io
import os

import requests
from docx.shared import Mm
from docxtpl import InlineImage, DocxTemplate

from BackStrawBerryPy.models import BaseModel
from BackStrawBerryPy.settings import BASE_DIR
from apps.Notas.models import NotaAlumno, EvidenciaNotaAlumno
from apps.Personas.models import Personal
from utils.functions import create_docx, docx_to_bytes

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


def reporte_notas(id_matricula):
    notas = NotaAlumno.objects.prefetch_related("evidencias").filter(
        alumno_aula_id=id_matricula,
        auth_estado=BaseModel.ACTIVO
    )

    imgs = EvidenciaNotaAlumno.objects.filter(
        nota_id__in=[nota.pk for nota in notas]
    ).values_list('url', flat=True)

    tpl = DocxTemplate(get_reporte('MATRIZ_INFORME.docx'))
    imgs_objs = dict()

    for index, img in enumerate(list(imgs)):
        response = requests.get(img, stream=True)
        image = io.BytesIO(response.content)
        my_image = InlineImage(tpl, image, width=Mm(100))
        imgs_objs.__setitem__(f'img{index + 1}', my_image)

    items = {
        'responsable': 'PRUEBA',
        'area_de_trabajo': 'PRUEBA2',
        'docente': 'PRUEBA3',
        'coordinador': 'PRUEBA4',
        'director': 'PRUEBA5',
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
    }
    tpl.render({**items, **imgs_objs})
    return docx_to_bytes(tpl)
