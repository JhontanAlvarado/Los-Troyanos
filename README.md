# Plantilla: Sistema de Gestión Clínica (Django)

## Lógica del Negocio
Este sistema está diseñado para gestionar el flujo básico de una clínica médica o consultorio independiente. Contempla el registro de **Pacientes**, la gestión de **Doctores** (con sus respectivas especialidades/habilidades) y el control interno de operaciones. 

## Arquitectura
El proyecto adopta un enfoque **"Local-First"**. Está optimizado para ejecutarse en servidores locales (ej. una computadora estándar en la recepción de la clínica) utilizando **SQLite**. Esta decisión arquitectónica permite a las pequeñas y medianas empresas tener un sistema de gestión de inventario, ventas o pacientes rápido y privado, eliminando los costos recurrentes de bases de datos o *hosting* en la nube.