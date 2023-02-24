from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProcesoCreateUpdateViewSet, ProcesoList, ProcesoDetail, CrearProceso

router = DefaultRouter()
router.register(r'upload', ProcesoCreateUpdateViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', CrearProceso.as_view()),
    path('list/', ProcesoList.as_view()),
    path('<int:pk>', ProcesoDetail.as_view()),
]