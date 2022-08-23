from django.db import models

class Coberturasalud(models.Model):
    denominacion=models.CharField(max_length=60)
    codigo=models.IntegerField()
    

class familia(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    dni=models.FloatField()
    extranjero=models.BooleanField()
    enfermedadbase=models.CharField(max_length=20)
    mail=models.EmailField()

class Obrasocial(models.Model):
    NombreOS=models.CharField(max_length=60)
    fecha_afiliacion= models.DateField
    plan=models.IntegerField()
    cargafamiliar= models.BooleanField

class trabajo(models.Model):
    empresa=models.CharField(max_length=60)
    antiguedad= models.IntegerField()
    profesion=models.IntegerField()
    contrato=models.CharField(max_length=60)

