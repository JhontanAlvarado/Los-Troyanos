from django.db import models

# 1. Modelo Base para Auditoría (Idioma)
class ModeloBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True 

# 2. Modelo Especialidad
class Especialidad(ModeloBase):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

# 3. Modelo Habilidad
class Habilidad(ModeloBase):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# 4. Modelo Paciente
class Paciente(ModeloBase):
    nombre = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

# 5. Modelo Doctor
class Doctor(ModeloBase):
    nombre = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField()
    antiguedad = models.PositiveIntegerField(help_text="Años de antigüedad")
    
    # Relaciones
    especialidad = models.ForeignKey(Especialidad, on_delete=models.RESTRICT, related_name="doctores")
    habilidades = models.ManyToManyField(Habilidad, related_name="doctores")
    pacientes = models.ManyToManyField(Paciente, related_name="doctores")

    def __str__(self):
        return self.nombre

# 5. Modelo Cita
class Cita(ModeloBase):
    paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE, related_name="citas")
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name="citas")
    fecha = models.DateTimeField()

    def __str__(self):
        return f"{self.paciente} - {self.doctor} - {self.fecha}"

    class Meta:
        unique_together = ('doctor', 'fecha')