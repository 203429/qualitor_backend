from django.urls import path
from django.conf.urls import include

from manual.views import ManualView,ManualDetail

urlpatterns = [
    path('list/', ManualView.as_view()),
    path('list/<int:pk>', ManualDetail.as_view()),
]
