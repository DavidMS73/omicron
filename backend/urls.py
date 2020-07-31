from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'profesores', views.ProfesorViewSet)
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'materias', views.MateriaViewSet)
router.register(r'criterios', views.CriterioViewSet)
router.register(r'temas', views.TemaViewSet)
router.register(r'actividades', views.ActividadViewSet)
router.register(r'cuadernos', views.CuadernoViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('actividades/createqr', views.CreateQRView.as_view(),
         name="songs-list-create"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
