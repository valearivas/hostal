from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}"

class Medico(models.Model):

    HORAS_DISPONIBLES = [ ('08:00:00', '08:00 AM'),    ('09:00:00', '09:00 AM'),    ('10:00:00', '10:00 AM'),    ('11:00:00', '11:00 AM'),    ('12:00:00', '12:00 PM'),    ('13:00:00', '01:00 PM'),    ('14:00:00', '02:00 PM'),    ('15:00:00', '03:00 PM'),    ('16:00:00', '04:00 PM'),    ('17:00:00', '05:00 PM'),]

    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name='ESPECIALIDAD')
   
    
    def __str__(self):
        return f"{self.nombres} {self.apellidos}"



HORAS_DISPONIBLES = [ ('08:00', '08:00 AM'),    ('09:00', '09:00 AM'),    ('10:00', '10:00 AM'),    ('11:00', '11:00 AM'),    ('12:00', '12:00 PM'),    ('13:00', '01:00 PM'),    ('14:00', '02:00 PM'),    ('15:00', '03:00 PM'),    ('16:00', '04:00 PM'),    ('17:00', '05:00 PM'),]
class HoraDisponible(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='horas_disponibles')
    dia = models.DateField(auto_now_add= False, auto_now= False, blank = True, null=True, verbose_name='dia')
    hora = models.CharField(choices=HORAS_DISPONIBLES, max_length=10, null=True, blank=True)


    def __str__(self):
        return f" {self.dia} {self.hora} "

class Reserva(models.Model):
    info = models.ForeignKey(HoraDisponible, on_delete=models.CASCADE, blank = True, null=True,related_name='reservas' )
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,related_name='usuario')
    confirmada = models.BooleanField(default=False,blank = True, null=True)
    
    def __str__(self):
        return f"{self.info.medico.nombres} {self.confirmada} {self.usuario}"