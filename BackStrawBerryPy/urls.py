# from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView
from graphql_jwt.decorators import jwt_cookie
from graphql_playground.views import GraphQLPlaygroundView

from BackStrawBerryPy.schema import schema
from apps.Personas import views

urls_reportes = [
    path('api/v1/reporte-nomina', views.get_reporte_nomina),
    path('api/v1/reporte-notas', views.get_reporte_notas),
    path('api/v1/reporte-matricula', views.get_reporte_matricula),
]

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/v1/', include(urls_api)),
    path('webpush/', include('webpush.urls')),
    path('graphql', csrf_exempt(jwt_cookie(FileUploadGraphQLView.as_view(graphiql=True, schema=schema)))),
    path('playground', csrf_exempt(jwt_cookie(GraphQLPlaygroundView.as_view(endpoint='graphql')))),
]
urlpatterns = urlpatterns + urls_reportes
