from django.contrib import admin
from django.urls import include, path,re_path
from .views import UserList

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', include('dj_rest_auth.registration.urls')),
    re_path('list/', UserList.as_view()),
]

# urlpatterns = [
#     path('registrar/',)
# ]