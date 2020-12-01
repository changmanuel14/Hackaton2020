from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    genero = models.CharField(max_length=1)
    fecha_nacimiento = models.DateField()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, null=True)
    sintomas = models.CharField(max_length=100)
