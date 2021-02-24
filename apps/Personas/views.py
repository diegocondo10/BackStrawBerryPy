# Create your views here.
from django.http import FileResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request

from apps.Personas.reportes import reporte_nomina, reporte_notas


@api_view(['POST', 'GET'])
def get_reporte_nomina(request):
    file = reporte_nomina()
    return FileResponse(
        file,
        as_attachment=True,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        filename='test.docx'
    )


@api_view(['POST', 'GET'])
def get_reporte_notas(request: Request):
    data: dict = request.data

    file = reporte_notas(
        id_matricula=data.get('id_matricula'),
        id_docente=data.get('id_docente'),
        area_trabajo=data.get('area_trabajo'),
        responsable=data.get('responsable'),
    )
    return FileResponse(
        file,
        as_attachment=True,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        filename='test.docx'
    )
