from apps.Personas.graphql.mutations import *


class PersonasMutations(graphene.ObjectType):
    create_persona = CreatePersonaMutation.Field()
    update_persona = UpdatePersonaMutation.Field()
    delete_persona = DeletePersonaMutation.Field()

    create_discapacidad = CreateDiscapacidadMutation.Field()
    update_discapacidad = UpdateDiscapacidadMutation.Field()
    delete_discapacidad = DeleteDiscapacidadMutation.Field()

    create_personal = CreatePersonalMutation.Field()
    update_personal = UpdatePersonalMutation.Field()
    delete_personal = DeletePersonalMutation.Field()

    create_Alumno = CreateAlumnoMutation.Field()
    update_Alumno = UpdateAlumnoMutation.Field()
    delete_Alumno = DeleteAlumnoMutation.Field()
