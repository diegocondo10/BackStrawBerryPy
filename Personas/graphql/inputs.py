import graphene


class PadreDeFamiliaInput(graphene.InputObjectType):
    identificacion = graphene.String()
    primer_nombre = graphene.String()
    segundo_nombre = graphene.String()
    primer_apellido = graphene.String()
    segundo_apellido = graphene.String()
