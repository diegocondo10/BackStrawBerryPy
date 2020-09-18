import graphene
import graphene_django

from Personas.graphql.types import PersonaType, DiscapacidadType, DocenteType, EstudianteType
from Personas.models import Persona, Discapacidad, Docente, Estudiante


class PersonasQueries(graphene.ObjectType):
    personas = graphene.List(PersonaType)
    persona = graphene.Field(PersonaType, id=graphene.ID(required=True))
    personas_no_docentes = graphene.List(PersonaType)
    personas_no_estudiantes = graphene.List(PersonaType)

    docentes = graphene.List(DocenteType)
    docente = graphene.Field(DocenteType, id=graphene.ID(required=True))

    estudiantes = graphene.List(EstudianteType)
    estudiante = graphene.Field(EstudianteType, id=graphene.ID(required=True))

    discapacidades = graphene.List(DiscapacidadType)
    discapacidad = graphene.Field(DiscapacidadType, id=graphene.ID(required=True))

    def resolve_personas(self, info, **kwargs):
        return Persona.objects.all().order_by("primer_apellido")

    def resolve_persona(self, info, id):
        return Persona.objects.filter(pk=id).first()

    def resolve_personas_no_docentes(self, info, **kwargs):
        personas_docentes = Docente.objects.values_list('persona_id').all()
        return Persona.objects.exclude(id__in=personas_docentes).order_by('primer_apellido')

    def resolve_personas_no_estudiantes(self, info, **kwargs):
        personas_estudiantes = Estudiante.objects.values_list('persona_id').all()
        return Persona.objects.exclude(id__in=personas_estudiantes).order_by('primer_apellido')

    def resolve_docentes(self, info):
        return Docente.objects.all().order_by('persona__primer_apellido')

    def resolve_docente(self, info, id):
        return Docente.objects.filter(pk=id).first()

    def resolve_estudiantes(self, info):
        return Estudiante.objects.all().order_by('persona__primer_apellido')

    def resolve_estudiante(self, info, id):
        return Estudiante.objects.filter(pk=id).first()

    def resolve_discapacidades(self, info, **kwargs):
        return Discapacidad.objects.all()

    def resolve_discapacidad(self, info, id):
        return Discapacidad.objects.filter(pk=id).first()
