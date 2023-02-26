from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PhaseCreateUpdateViewSet, PhaseList, PhaseDetail, CrearPhase

router = DefaultRouter()
router.register(r'upload', PhaseCreateUpdateViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', CrearPhase.as_view()),
    path('list/', PhaseList.as_view()),
    path('<int:pk>', PhaseDetail.as_view()),
]