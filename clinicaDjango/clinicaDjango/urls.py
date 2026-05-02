from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_especialidades, name='index'),
    path('especialidades/<int:especialidad_id>/', views.show_especialidad, name='detail'),
    path('especialidades/<int:especialidad_id>/doctores', views.index_doctores, name='doctores'),
    path('doctores/<int:doctor_id>', views.show_doctor, name='doctor'),
    path('habilidades/<int:habilidad_id>', views.show_habilidad, name='habilidad'),
    path('pacientes/<int:paciente_id>', views.show_paciente, name='paciente'),
]
