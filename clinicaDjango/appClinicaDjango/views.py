from django.shortcuts import render, get_object_or_404
from .models import Especialidad, Doctor, Habilidad, Paciente

def index_especialidades(request):
    especialidades = Especialidad.objects.all().order_by('nombre')
    context = {'especialidades': especialidades}
    return render(request, 'index.html', context)

def show_especialidad(request, id):
    especialidad = get_object_or_404(Especialidad, pk=id)
    context = {'especialidad': especialidad}
    return render(request, 'detail.html', context)

def index_doctores(request, id):
    especialidad = get_object_or_404(Especialidad, pk=id)
    doctores = especialidad.doctores.all() # Usamos el related_name
    context = {'especialidad': especialidad, 'doctores': doctores}
    return render(request, 'doctores.html', context)

def show_doctor(request, id):
    doctor = get_object_or_404(Doctor, pk=id)
    context = {'doctor': doctor}
    return render(request, 'doctor.html', context)

def show_habilidad(request, id):
    habilidad = get_object_or_404(Habilidad, pk=id)
    context = {'habilidad': habilidad}
    return render(request, 'habilidad.html', context)

def show_paciente(request, id):
    paciente = get_object_or_404(Paciente, pk=id)
    context = {'paciente': paciente}
    return render(request, 'paciente.html', context)