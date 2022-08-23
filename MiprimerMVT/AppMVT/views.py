from django.http import HttpResponse
from django.shortcuts import render
from .models import Coberturasalud, familia, Obrasocial, trabajo


def Coberturasalud(request):

    Cobertura=Coberturasalud(denominacion="Swiss_Medical", codigo=3259)
    Cobertura.save()
    texto=f"Base de Coberturas de Salud familiar creado: nombre: {Cobertura.denominacion} codigo: {Cobertura.codigo}"
    return HttpResponse(texto)

def familia(request):

    Familia=familia(nombre="Romina", apellido="Galeano", dni=27549978, extranjero="False", enfermedadbase="Asma", mail="rommibu@gmail.com")
    Familia.save()
    texto=f"Nuevo familiar agregado: nombre: {Familia.nombre} apellido: {Familia.apellido} dni: {Familia.dni} extranjero: {Familia.extranjero} enfermedadbase: {Familia.enfermedadbase} mail: {Familia.mail}"
    return HttpResponse(texto) 

def Obrasocial(request):

    InfoOS=Obrasocial(nombreOS="Swiss_medical", fecha_afiliacion= 15-2-2019, plan="Premium", cargafamiliar= "hermano")
    InfoOS.save()
    texto=f"Nueva descripcion de Obra Social: nombre: {InfoOS.nombre} fecha_afiliacion: {InfoOS.fecha} plan: {InfoOS.plan} cargafamiliar: {InfoOS.cargafamiliar}"
    return HttpResponse(texto)

def trabajo(request):

    Trabajo=trabajo(empresa="Naranja", antiguedad= 22, profesion="Analista", contrato="Fija")
    Trabajo.save()
    texto=f"Descripcion de trabajo agregado: empresa{Trabajo.empresa} antiguedad: {Trabajo.antiguedad} profesion: {Trabajo.profesion} contrato{Trabajo.contrato}"
    return HttpResponse(texto)

