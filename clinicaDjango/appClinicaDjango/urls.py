from django.urls import path
from . import views

app_name = 'appClinicaDjango'

urlpatterns = [
    # Página principal con lista de especialidades
    path('', views.index_especialidades, name='index_especialidades'),
    
    # Detalle de especialidad
    path('especialidades/<int:id>/', views.show_especialidad, name='show_especialidad'),
    
    # Doctores de una especialidad específica
    path('especialidades/<int:id>/doctores/', views.index_doctores, name='index_doctores'),
    
    # Detalle de doctor
    path('doctores/<int:id>/', views.show_doctor, name='show_doctor'),
    
    # Detalle de habilidad
    path('habilidades/<int:id>/', views.show_habilidad, name='show_habilidad'),
    
    # Detalle de paciente
    path('pacientes/<int:id>/', views.show_paciente, name='show_paciente'),
]