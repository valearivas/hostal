from dataclasses import fields
from django import forms
from django.forms import ModelForm, DateInput
from .models import *

from datetime import datetime, timedelta
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ReservaForm(forms.Form):
    especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all(), label='Seleccionar Especialidad')
    medico = forms.ModelChoiceField(queryset=Medico.objects.all(), label='Seleccionar Médico')
    hora = forms.ChoiceField(label='Seleccionar Hora')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hora'].choices = []  # Inicializar las opciones de hora como una lista vacía

    def actualizar_doctores(self, especialidad_id):
        especialidad = Especialidad.objects.get(pk=especialidad_id)
        medicos = Medico.objects.filter(especialidad=especialidad)
        opciones_medicos = [(medico.id, medico) for medico in medicos]
        self.fields['medico'].choices = opciones_medicos

    def actualizar_horas_disponibles(self, medico_id):
        medico = Medico.objects.get(pk=medico_id)
        horas_disponibles = HoraDisponible.objects.filter(medico=medico)
        opciones_horas = [(hora.id, hora) for hora in horas_disponibles]
        self.fields['hora'].choices = opciones_horas
    
    def hora_reserva(self,id_horaDisponible ):
        id_horaDisponible = HoraDisponible.objects.get(pk=id_horaDisponible)
        self.fields = id_horaDisponible


    
    class Meta:
        model = Reserva
        fields = ['info']


class MedicoForm(forms.ModelForm):
    DIAS_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    dias_disponibles = forms.MultipleChoiceField(choices=DIAS_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta: 
        model = Medico
        fields = ['nombres', 'apellidos', 'especialidad', 'dias_disponibles']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]