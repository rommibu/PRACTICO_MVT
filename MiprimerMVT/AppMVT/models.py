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

"""class Obrasocial(models.Model):
    nombreOS=models.CharField(max_length=60)
    fecha_afiliacion= models.DateField()
    plan=models.CharField(max_length=10)
    cargafamiliar= models.CharField(max_length=15)"""

class trabajo(models.Model):
    empresa=models.CharField(max_length=60)
    antiguedad= models.IntegerField()
    profesion=models.CharField(max_length=50)
    contrato=models.CharField(max_length=60)

