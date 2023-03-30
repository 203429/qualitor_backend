from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PhaseCreateUpdateViewSet, PhaseList, PhaseDetail, CrearPhase, PhasePerProject

router = DefaultRouter()
router.register(r'upload', PhaseCreateUpdateViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', CrearPhase.as_view()),
    path('lista/', PhaseList.as_view()),
    path('detalle/<int:pk>', PhaseDetail.as_view()),
    path('proyecto/<int:id_proyecto>', PhasePerProject.as_view()),
]