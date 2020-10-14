import graphene
from Matriculas.graphql.mutatios import *


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
