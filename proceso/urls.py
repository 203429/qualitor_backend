from django.urls import path
from django.conf.urls import include

from proceso.views import ProcesoView,ProcesoDetail
urlpatterns = [
    path('list/', ProcesoView.as_view()),
    path('list/<int:pk>', ProcesoDetail.as_view()),
]