from django.shortcuts import render, redirect
from .forms import * 
from .models import *   
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View



# Create your views here.
def home(request):
    return render(request, 'dos_alamos/home.html')


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

    return render(request, 'dos_alamos/reservar/crear_r.html', datos)


@login_required
def confirmar_r(request):

    if request.method == 'POST':

        hora = HoraDisponible.objects.get(pk=request.POST['hora_disponible'])

        reserva = {"medico": request.POST['medico'],"hora":request.POST['hora'],"dia":request.POST['dia'],"usuario":request.user}
        #value=request.POST['dia']
        print(reserva)
    
    return render(request, 'dos_alamos/reservar/confirmar_r.html', {'reserva': reserva})


@login_required
def confirmar_r_post(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user, confirmada=False)
    reserva.confirmada = True
    reserva.save()
    return redirect('read_r')


def read_r(request):
    if request.user.username != 'paula':
        reservas = Reserva.objects.filter(usuario=request.user)

    else:
        reservas = Reserva.objects.all()
        
    datos = {
       
        'reserva': reservas
        
    }
    
    return render(request,'dos_alamos/reservar/read_r.html', datos)


def modify_r(request, id):

    reserva = Reserva.objects.get(id = id)

    datos = {
        'form': ReservaForm(instance=reserva)
    }

    if request.method == 'POST':
        formulario = ReservaForm(data=request.POST, instance=reserva, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="read_r")
        datos["form"] = formulario
            

    return render(request, 'dos_alamos/reservar/modify_r.html', datos)


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

    return render(request,'dos_alamos/medico/crear_m.html', datos)


def read_m(request):
    medico = Medico.objects.all()

    datos = {
       
        'medico': medico
        
    }
    
    return render(request,'dos_alamos/medico/read_m.html', datos)

def eliminar_m(request,id):
    medico = Medico.objects.get(id =id)
    medico.delete()
    return redirect(to = 'read_m')


