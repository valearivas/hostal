from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', home, name="home"),
    path('login/', login, name='login'),
    path('registro/', registro, name="registro"),
    path('crear_r/', crear_r, name='crear_r'),
    path('confirmar_r/', confirmar_r, name='confirmar_r'),
    path('confirmar_r_post/<int:reserva_id>/', confirmar_r_post, name='confirmar_r_post'),
    path('read_r/', read_r ,name='read_r'),
    path('modify_r/<id>/',modify_r,name='modify_r'),
    path('eliminar_r/<id>/',eliminar_r,name='eliminar_r'),
    path('crear_m/',crear_m,name='crear_m'),
    path('read_m/',read_m,name='read_m'),
    path('eliminar_m/<id>/',eliminar_m,name='eliminar_m'),
    
    
    ]