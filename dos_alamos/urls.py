from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name='login'),
    path('registro/', registro, name="registro"),
    path('crear_r/', crear_r, name='crear_r'),
    path('confirmar_r/', confirmar_r, name='confirmar_r'),
    path('confirmar_r_post/', confirmar_r_post, name='confirmar_r_post'),
    path('read_r/', read_r ,name='read_r'),
    path('modify_r/<int:reserva_id>/', views.modify_r, name='modify_r'),
    path('eliminar_r/<id>/',eliminar_r,name='eliminar_r'),
    path('crear_m/',crear_m,name='crear_m'),
    path('crear_hora_disponible/', crear_hora_disponible, name='crear_hora_disponible'),
    path('read_m/',read_m,name='read_m'),
    path('eliminar_m/<id>/',eliminar_m,name='eliminar_m'),
    
    
    ]