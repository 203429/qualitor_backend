from django.urls import path
from django.conf.urls import include

from documento.views import DocumentoView,DocumentoDetail
urlpatterns = [
    path('list/', DocumentoView.as_view()),
    path('list/<int:pk>', DocumentoDetail.as_view()),
]