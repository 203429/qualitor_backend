from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProcesoCreateUpdateViewSet, ProcesoList, ProcesoDetail

router = DefaultRouter()
router.register(r'upload', ProcesoCreateUpdateViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('list/', ProcesoList.as_view()),
    path('<int:pk>', ProcesoDetail.as_view()),
]