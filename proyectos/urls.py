from django.urls import path
from django.conf.urls import include

from proyectos.views import ProyectoView,ProyectoDetail,CrearProyecto,EliminarProyecto
urlpatterns = [
    path('lista/', ProyectoView.as_view()),
    path('detalle/<int:pk>', ProyectoDetail.as_view()),
    path('crear/', CrearProyecto.as_view()),
    path('eliminar/<int:id_users>', EliminarProyecto.as_view()),
]