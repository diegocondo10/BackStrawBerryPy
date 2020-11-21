import graphene
from apps.Matriculas.graphql.mutatios import *


class MatriculasMutations(graphene.ObjectType):
    create_periodo_lectivo = CreatePeriodoLectivoMutation.Field()
    update_periodo_lectivo = UpdatePeriodoLectivoMutation.Field()
    delete_periodo_lectivo = DeletePeriodoLectivoMutation.Field()

    create_aula = CreateAulaMutation.Field()
    update_aula = UpdateAulaMutation.Field()
    delete_aula = DeleteAulaMutation.Field()

    create_materia = CreateMateriaMutation.Field()
    update_materia = UpdateMateriaMutation.Field()
    delete_materia = DeleteMateriaMutation.Field()

    create_alumno_aula = CreateAlumnoAulaMutation.Field()
    update_alumno_aula = UpdateAlumnoAulaMutation.Field()
    delete_alumno_aula = DeleteAlumnoAulaMutation.Field()

    # create_nota_materia = CreateNotaMateria.Field()
    # update_nota_materia = UpdateNotaMateria.Field()
    # delete_nota_materia = DeleteNotaMateria.Field()
