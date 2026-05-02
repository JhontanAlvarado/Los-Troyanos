from django.db import models

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Habilidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidad)
    pacientes = models.ManyToManyField(Paciente, blank=True)
    nombre = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    antiguedad = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre