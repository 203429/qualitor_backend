from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProcesoCreateUpdateViewSet, ProcesoList, ProcesoDetail, CrearProceso, ProcesoPerPhase

router = DefaultRouter()
router.register(r'upload', ProcesoCreateUpdateViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', CrearProceso.as_view()),
    path('lista/', ProcesoList.as_view()),
    path('detalle/<int:pk>', ProcesoDetail.as_view()),
    path('fase/<int:id_fase>', ProcesoPerPhase.as_view()),
]