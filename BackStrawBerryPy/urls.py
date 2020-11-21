"""BackStrawBerryPy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from graphql_playground.views import GraphQLPlaygroundView

from BackStrawBerryPy.schema import schema
'''
from apps.Personas import views
urls_api = [
    path('auth/', include('apps.Auth.router')),
]
'''

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('api/v1/', include(urls_api)),
    path('graphql', csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True, schema=schema)))),
    path('playground', csrf_exempt(jwt_cookie(GraphQLPlaygroundView.as_view(endpoint='graphql')))),
]
