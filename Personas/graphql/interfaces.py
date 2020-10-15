import graphene


class PadreDeFamiliaInterface(graphene.AbstractType):
    identificacion = graphene.String()
    primer_nombre = graphene.String()
    segundo_nombre = graphene.String()
    primer_apellido = graphene.String()
    segundo_apellido = graphene.String()
    celular = graphene.String()
    telefono = graphene.String()
    ocupacion = graphene.String()
    direccion = graphene.String()
