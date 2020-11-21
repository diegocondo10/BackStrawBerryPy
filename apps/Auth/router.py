from rest_framework import routers

from apps.Auth.views import AplicacionViewSet, GrupoViewSet, PermisoViewSet, UsuarioViewset

router = routers.SimpleRouter()
router.register(r'aplicaciones', AplicacionViewSet)
router.register(r'permisos', PermisoViewSet)
router.register(r'grupos', GrupoViewSet)
router.register(r'usuarios', UsuarioViewset)

urlpatterns = router.urls
