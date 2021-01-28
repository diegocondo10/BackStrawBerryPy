import graphene
from graphene.types.generic import GenericScalar


class ResponseType(graphene.ObjectType):
    data = graphene.types.generic.GenericScalar()
    meta_data = graphene.types.generic.GenericScalar()


class ErrorType(graphene.ObjectType):
    codigo = graphene.Int()
    mensaje = graphene.String()
    mensajes = graphene.List(graphene.String)
    descripcion = graphene.String()
