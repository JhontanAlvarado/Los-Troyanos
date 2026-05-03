from django.contrib import admin
from .models import Especialidad, Habilidad, Paciente, Doctor, Cita

# Registramos los modelos simples   
admin.site.register(Especialidad)
admin.site.register(Habilidad)
admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Cita)