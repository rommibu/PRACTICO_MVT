from django.db import models


class Coberturasalud(models.Model):
    denominacion=models.CharField(max_length=60)
    codigo=models.IntegerField()
    fecha_creacion=models.DateField()

    def __str__(self):
        return self.denominacion+" "+str(self.denominacion)
    

class familia(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    dni=models.FloatField()
    extranjero=models.BooleanField()
    enfermedadbase=models.CharField(max_length=20)
    mail=models.EmailField()

    def __str__(self):
        return self.dni+" "+str(self.dni)


class trabajo(models.Model):
    empresa=models.CharField(max_length=60)
    antiguedad= models.IntegerField()
    profesion=models.CharField(max_length=50)
    contrato=models.CharField(max_length=60)

