# Create your views here.
from django.http import FileResponse
from rest_framework.decorators import api_view

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
def get_reporte_notas(request, id_matricula):
    file = reporte_notas(id_matricula)
    return FileResponse(
        file,
        as_attachment=True,
        content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        filename='test.docx'
    )
