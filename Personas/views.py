# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from Personas.models import Persona


@api_view(['GET'])
def mis_alumnos(request: Request, identificacion):
    docente = Persona.objects.filter(identificacion=identificacion).first()

    return Response({
        'transaccion': True,
        'docente': docente.__str__(),
        'data': {
            'alumnos': []
        }
    })
