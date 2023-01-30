from django.urls import path
from django.conf.urls import include

from role.views import RoleList, RoleDetail

urlpatterns = [
    path('list/', RoleList.as_view()),
    path('list/<int:pk>', RoleDetail.as_view()),
]