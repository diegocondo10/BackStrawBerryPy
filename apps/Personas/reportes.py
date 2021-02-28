import calendar
import io
import json
import os
from datetime import date

import pandas as pd
import requests
from django.utils.translation import gettext as _
from docx.shared import Mm
from docxtpl import InlineImage, DocxTemplate

from BackStrawBerryPy.models import BaseModel
from BackStrawBerryPy.settings import BASE_DIR
from apps.Matriculas.models import AlumnoAula
from apps.Notas.models import NotaAlumno, EvidenciaNotaAlumno
from apps.Personas.models import Personal
from utils.functions import create_docx, docx_to_bytes, create_docx_bytes, get_edad, concat_if_exist, get_ordinal_num

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
    alumno = matricula.alumno

    return create_docx_bytes(
        file=get_reporte("FichaInscripcion.docx"),
        context={
            'anio': date.today().year,
            'apellidos': persona.get_apellidos(),
            'nombres': persona.get_nombres(),
            'lugar': persona.direccion_domiciliaria,
            'fecha_n': persona.fecha_nacimiento.strftime('%d/%m/%Y'),
            'edad': get_edad(persona.fecha_nacimiento),
            'cedula': persona.identificacion,
            'conadis': persona.carnet_conadis,
            'nivel_a': _(get_ordinal_num(aula.grado)),
            'promovido': _(get_ordinal_num(aula.grado)),
            'tratamiento': matricula.tratamiento,
            'diagnostico': matricula.diagnostico_clinico,
            # INFORMACION DEL PADRE
            'apellidos_p': concat_if_exist(alumno.padre.get('primer_apellido'), alumno.padre.get('segundo_apellido')),
            'nombres_p': concat_if_exist(alumno.padre.get('primer_nombre'), alumno.padre.get('segundo_nombre')),
            'cedula_p': alumno.padre.get('identificacion'),
            'ocupacion_p': alumno.padre.get('ocupacion'),
            'direccion_p': alumno.padre.get('direccion'),
            'telefono_p': alumno.padre.get('telefono'),
            'celular_p': alumno.padre.get('celular'),
            # INFORMACION DE LA MADRE
            'apellidos_m': concat_if_exist(alumno.madre.get('primer_apellido'), alumno.madre.get('segundo_apellido')),
            'nombres_m': concat_if_exist(alumno.madre.get('primer_nombre'), alumno.madre.get('segundo_nombre')),
            'cedula_m': alumno.madre.get('identificacion'),
            'ocupacion_m': alumno.madre.get('ocupacion'),
            'direccion_m': alumno.madre.get('direccion'),
            'telefono_m': alumno.madre.get('telefono'),
            'celular_m': alumno.madre.get('celular'),
            'correo': persona.correo,
            'direccion': persona.direccion_domiciliaria,
            'provincia': persona.provincia_residencia,
            'canton': persona.canton_residencia,
            'parroquia': persona.parroquia_residencia,
            'sector': persona.sector,
            # CONTACTO_EMERGENCIA
            'nombre_emergencia': alumno.contacto_emergencia.get('nombres'),
            'contacto': alumno.contacto_emergencia.get('contacto'),
            'nombre_representante': alumno.representante.get('nombres'),
            # MATRICULA
            'matricula': matricula.numero_matricula,
            'aporte': f"${matricula.aporte_voluntario}",
            'fecha_inscripcion': matricula.created_at.strftime('%d/%m/%Y')
        }
    )


def set_column(context, column, value):
    array = context.get(column)
    array.append(value)
    context[column] = array


def reporte_general_total_alumnos(id_periodo):
    matriculas = AlumnoAula.objects \
        .select_related('alumno', 'alumno__persona', 'aula', 'aula__periodo') \
        .filter(auth_estado=BaseModel.ACTIVO, aula__periodo__id__in=[id_periodo])

    # .values() \
    # .select_related('persona') \
    context = {
        "No": [],
        "NOMBRE DEL USUARIO": [],
        "AMIE": [],
        "MIES": [],
        "NIVELES": [],
        "FECHA DE INGRESO": [],
        "PAIS DE NACIMIENTO": [],
        "FECHA DE NACIMIENTO USUARIO": [],
        "EDAD": [],
        # "MESES": [],
        "CEDULA O PASAPORTE": [],
        "GENERO": [],
        "ESTADO CIVIL": [],
        "CARNET DE DISCAPACIDAD": [],
        "Nª DE REGISTRO CARNET": [],
        "TIPO DE DISCAPACIDAD": [],
        "PORCENTAJE": [],
        "ETNIA": [],
        "HISTORIA CLINICA": [],
        "TIPO DE SANGRE": [],
        "DIAGNOSTICO CLINICO": [],
        "TRASTORNOS ASOCIADOS": [],
        "GRADO DE DEPENDENCIA": [],
        "REPRESENTANTE": [],
        "NOMBRE PADRE": [],
        "CI PADRE": [],
        "NOMBRE MADRE": [],
        "C.I MADRE": [],
        "TIPO DE FLIA": [],
        "BONO": [],
        "TIPO DE BONO": [],
        "AFILICACIÓN IESS": [],
        "QUINTIL DE POBREZA": [],
        "PAIS": [],
        "PROVINCIA": [],
        "CANTON": [],
        "PARROQUIA": [],
        "DIRECCION": [],
        "TELEFONO DOMICILIO": [],
        "CELULAR 1": [],
        "CELULAR 2": [],
    }

    for index, matricula in enumerate(matriculas):
        alumno = matricula.alumno
        persona = alumno.persona
        aula = matricula.aula
        # periodo = aula.periodo
        set_column(context, "No", index + 1)
        set_column(context, "NOMBRE DEL USUARIO", persona.get_nombres_apellidos())
        set_column(context, "AMIE", matricula.amie)
        set_column(context, "MIES", matricula.mies)
        set_column(context, "NIVELES", aula.nombre)
        set_column(context, "FECHA DE INGRESO", alumno.created_at.strftime('%d/%m/%Y'))
        set_column(context, "PAIS DE NACIMIENTO", f"{persona.pais_nacimiento}")
        set_column(context, "FECHA DE NACIMIENTO USUARIO", persona.fecha_nacimiento.strftime('%d/%m/%Y'))
        set_column(context, "EDAD", persona.get_edad())
        set_column(context, "CEDULA O PASAPORTE", persona.identificacion)
        set_column(context, "GENERO", persona.genero)
        set_column(context, "ESTADO CIVIL", persona.estado_civil)
        set_column(context, "CARNET DE DISCAPACIDAD", persona.tiene_discapacidad)
        set_column(context, "Nª DE REGISTRO CARNET", persona.carnet_conadis)
        set_column(context, "TIPO DE DISCAPACIDAD", "")
        set_column(context, "PORCENTAJE", persona.porcentaje_discapacidad)
        set_column(context, "ETNIA", persona.etnia)
        set_column(context, "HISTORIA CLINICA", alumno.historia_clinica)
        set_column(context, "TIPO DE SANGRE", persona.tipo_sangre)
        set_column(context, "DIAGNOSTICO CLINICO", matricula.diagnostico_clinico)
        set_column(context, "TRASTORNOS ASOCIADOS", alumno.trastornos_asociados)
        set_column(context, "GRADO DE DEPENDENCIA", matricula.grado_dependencia)
        set_column(context, "REPRESENTANTE", alumno.representante.get("parentesco", ""))  # TODO: mapp this value
        set_column(context, "NOMBRE PADRE", alumno.map_padres().get('apellidos_nombres'))
        set_column(context, "CI PADRE", alumno.padre.get('identificacion'))
        set_column(context, "NOMBRE MADRE", alumno.map_padres("madre").get("apellidos_nombres"))
        set_column(context, "C.I MADRE", alumno.madre.get("identificacion"))
        set_column(context, "TIPO DE FLIA", matricula.tipo_familia)
        set_column(context, "BONO", alumno.bono)
        set_column(context, "TIPO DE BONO", alumno.tipo_bono)
        set_column(context, "AFILICACIÓN IESS", alumno.afiliacion_iess)
        set_column(context, "QUINTIL DE POBREZA", alumno.quintil_pobreza)
        set_column(context, "PAIS", persona.pais_residencia)
        set_column(context, "PROVINCIA", persona.provincia_residencia)
        set_column(context, "CANTON", persona.canton_residencia)
        set_column(context, "PARROQUIA", persona.parroquia_residencia)
        set_column(context, "DIRECCION", persona.direccion_domiciliaria)
        set_column(context, "TELEFONO DOMICILIO", persona.telefono)
        set_column(context, "CELULAR 1", persona.celular_uno)
        set_column(context, "CELULAR 2", persona.celular_dos)

    print(json.dumps(context))
    df = pd.DataFrame(context)
    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, datetime_format='mmm d yyyy hh:mm', date_format='dd mmmm yyyy', ) as writer:
        df.to_excel(writer, sheet_name="BASE ACTUALIZADA", index=False)
    buffer.seek(0)
    return buffer
