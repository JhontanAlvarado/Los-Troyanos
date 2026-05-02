# Plantilla: Sistema de Gestión Clínica (Django)
# Clínica Django

Proyecto web desarrollado con Django para la gestión de una clínica médica.

## Integrantes
- Dana Sainz Rubin de Celis
- Andree Villca Torrico
- Jhosselin Sthaicy Bustamante Escobar
- Jhonatan Alvarado Mamani

## Requisitos
- Python 3.12
- Django 6.0

## Instalación
1. Activar entorno virtual: source env/bin/activate
2. Instalar dependencias: pip install -r requirements.txt
3. Ejecutar servidor: python manage.py runserver
## Lógica del Negocio
Este sistema está diseñado para gestionar el flujo básico de una clínica médica o consultorio independiente. Contempla el registro de **Pacientes**, la gestión de **Doctores** (con sus respectivas especialidades/habilidades) y el control interno de operaciones. 

## Arquitectura
El proyecto adopta un enfoque **"Local-First"**. Está optimizado para ejecutarse en servidores locales (ej. una computadora estándar en la recepción de la clínica) utilizando **SQLite**. Esta decisión arquitectónica permite a las pequeñas y medianas empresas tener un sistema de gestión de inventario, ventas o pacientes rápido y privado, eliminando los costos recurrentes de bases de datos o *hosting* en la nube.
