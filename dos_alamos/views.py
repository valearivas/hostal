from django.shortcuts import render, redirect
from .forms import * 
from .models import *   
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View



# Create your views here.
def home(request):
    return render(request, 'hostal/home.html')


def registro(request):
   
    datos = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/registro.html', datos)


from django.shortcuts import render, redirect, get_object_or_404

@login_required
def crear_r(request):
    datos = {}
    formulario = ReservaForm()

    if request.method == 'POST':

        print(request.POST['dia'])

        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            reserva = formulario.save(commit=False)
            reserva.info = HoraDisponible.objects.get(pk=request.POST['hora_disponible'])
            reserva.usuario = request.user
            reserva.confirmada = True
            reserva.save()
            return redirect('read_r')

    if 'especialidad' in request.GET:
        especialidad_id = request.GET['especialidad']
        formulario.actualizar_doctores(especialidad_id)
        medicos_especialidad = Medico.objects.filter(especialidad_id=especialidad_id)
        datos['medicos_especialidad'] = medicos_especialidad

    if 'medico' in request.GET:
        medico_id = request.GET['medico']
        formulario.actualizar_horas_disponibles(medico_id)
        horas_disponibles = HoraDisponible.objects.filter(medico_id=medico_id)

        fechas_horas_disponibles = []
        for hora_disponible in horas_disponibles:
            fechas_horas_disponibles.append({
                'id': hora_disponible.id,
                'fecha': hora_disponible.dia.strftime('%Y-%m-%d'),
                'hora': hora_disponible.hora,
                'medico': hora_disponible.medico,
            })

        datos['fechas_horas_disponibles'] = fechas_horas_disponibles
    
    datos['form'] = formulario
    datos['medicos'] = Medico.objects.all()

    return render(request, 'hostal/reservar/crear_r.html', datos)


@login_required
def confirmar_r(request):

    if request.method == 'POST':
        reserva = {"medico": request.POST['medico'],
                   "hora":request.POST['hora'],
                   "dia":request.POST['dia'],
                   "usuario":request.user, 
                   "hora_id": request.POST['hora_disponible']}
       
    
        
    return render(request, 'hostal/reservar/confirmar_r.html', {'reserva' :reserva })


@login_required
def confirmar_r_post(request):
    if request.method == 'POST':
        reserva = Reserva(info_id=request.POST['hora_disponible'], usuario=request.user, confirmada=True)
        reserva.save()
        datos = {'mensaje': 'Guardado exitosamente'}  # Agrega el mensaje de éxito al diccionario 'datos'
        return render(request, 'hostal/reservar/confirmar_r.html' ,datos)



def read_r(request):
    if request.user.username != 'paula':
        reservas = Reserva.objects.filter(usuario=request.user)

    else:
        reservas = Reserva.objects.all()
        
    datos = {
       
        'reserva': reservas
        
    }
    
    return render(request,'hostal/reservar/read_r.html', datos)


@login_required
def modify_r(request, reserva_id):
    datos = {}
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    formulario = ReservaForm(instance=reserva)

    if request.method == 'POST':
        formulario = ReservaForm(request.POST, instance=reserva)
        if formulario.is_valid():
            reserva = formulario.save(commit=False)
            reserva.info = HoraDisponible.objects.get(pk=request.POST['hora_disponible'])
            reserva.usuario = request.user
            reserva.confirmada = True
            reserva.save()
            return redirect('read_r')

    

    datos['form'] = formulario
 

    return render(request, 'hostal/reservar/modify_r.html', datos)



def eliminar_r(request,id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect(to = 'read_r')



def crear_m(request):

    datos = {
        'form' : MedicoForm()
    }
    if request.method == 'POST':
        formulario = MedicoForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado exitosamente'

    return render(request,'hostal/medico/crear_m.html', datos)


def crear_hora_disponible(request):

    datos = {
        'form' : HoraDisponibleForm()
    }
    if request.method == 'POST':
        formulario = HoraDisponibleForm(request.POST)
        
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Guardado exitosamente'

    return render(request,'hostal/medico/crear_hora_disponible.html', datos)



def read_m(request):
    medico = Medico.objects.all()

    datos = {
       
        'medico': medico
        
    }
    
    return render(request,'hostal/medico/read_m.html', datos)

def eliminar_m(request,id):
    medico = Medico.objects.get(id =id)
    medico.delete()
    return redirect(to = 'read_m')


