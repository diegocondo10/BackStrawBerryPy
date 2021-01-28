import graphene_django_optimizer as gql_optimizer

from apps.Matriculas.models import Aula, PeriodoLectivo, AlumnoAula
from apps.Personas.graphql.types import *


class PersonasQueries(graphene.ObjectType):
    personas = graphene.List(PersonaType)
    persona = graphene.Field(PersonaType, id=graphene.ID(required=True))
    personas_no_docentes = graphene.List(PersonaType)
    personas_no_alumnos = graphene.List(PersonaType)

    alumnos_sin_matricula = graphene.List(AlumnoType)

    funciones_personal = graphene.List(FuncionPersonalType)
    # funcion_persona = graphene.Field(FuncionPersonalType, id=graphene.ID(required=True))

    personal_all = graphene.List(PersonalType)
    personal = graphene.Field(PersonalType, id=graphene.ID(required=True))
    personal_by_funciones = graphene.List(PersonalType, funciones=graphene.List(graphene.String, required=True))

    alumnos = graphene.List(AlumnoType)
    alumno = graphene.Field(AlumnoType, id=graphene.ID(required=True))

    discapacidades = graphene.List(DiscapacidadType)
    discapacidad = graphene.Field(DiscapacidadType, id=graphene.ID(required=True))

    def resolve_funciones_personal(self, info, **kwargs):
        return FuncionPersonal.objects.all()

    def resolve_personas(self, info, **kwargs):
        return gql_optimizer.query(Persona.objects.all().order_by("primer_apellido"), info)

    def resolve_persona(self, info, id):
        return Persona.objects.filter(pk=id).first()

    def resolve_personas_no_personal(self, info, **kwargs):
        personas_personal = Personal.objects.values_list('persona_id').all()
        return Persona.objects.exclude(id__in=personas_personal).order_by('primer_apellido')

    def resolve_personas_no_alumnos(self, info, **kwargs):
        personas_alumnoss = Alumno.objects.values_list('persona_id').all()
        return Persona.objects.exclude(id__in=personas_alumnoss).order_by('primer_apellido')

    def resolve_alumnos_sin_matricula(self, info, **kwargs):
        # alumnos = gql_optimizer.query(
        #     Alumno.objects.raw('''
        #         SELECT * FROM "Alumnos" WHERE "Alumnos"."id" NOT IN (
        #             SELECT "Alumnos"."id" FROM "Alumnos"
        #                     INNER JOIN "AlumnoAulas" ON "Alumnos"."id" = "AlumnoAulas".alumno_id
        #                     INNER JOIN "Aulas" ON "AlumnoAulas".aula_id = "Aulas"."id"
        #                     INNER JOIN "PeriodoLectivos" ON "Aulas".periodo_id = "PeriodoLectivos"."id"
        #                 WHERE "PeriodoLectivos".estado = %s
        #         )
        #         ''', [PeriodoLectivo.EstadosPeriodo.CERRADO.value]),
        #     info
        # )

        alumnos_matriculados = AlumnoAula.objects.values_list('alumno_id').filter(
            aula__periodo__estado=PeriodoLectivo.EstadosPeriodo.ABIERTO.value
        )

        return gql_optimizer.query(Alumno.objects.exclude(id__in=alumnos_matriculados), info)

    def resolve_personal_all(self, info):
        return gql_optimizer.query(Personal.objects.all().order_by('persona__primer_apellido'), info)

    def resolve_personal(self, info, id):
        return Personal.objects.filter(pk=id).first()

    def resolve_personal_by_funciones(self, info, funciones):
        return gql_optimizer.query(Personal.objects.filter(funciones__nombre__in=funciones), info)

    def resolve_alumnos(self, info):
        return Alumno.objects.all().order_by('persona__primer_apellido')

    def resolve_alumno(self, info, id):
        return Alumno.objects.filter(pk=id).first()

    def resolve_discapacidades(self, info, **kwargs):
        return gql_optimizer.query(Discapacidad.objects.all(), info)
        # return Discapacidad.objects.all()

    def resolve_discapacidad(self, info, id):
        return Discapacidad.objects.filter(pk=id).first()
