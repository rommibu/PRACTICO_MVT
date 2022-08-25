from django.http import HttpResponse
from django.shortcuts import render
from .models import Coberturasalud, familia, trabajo
import datetime

def Cobertura_salud(request):
    print("Empieza la funcion!")
    Cobertura=Coberturasalud(denominacion="Medife", codigo=3624) 
    print("cree objeto cobertura")
    print(Cobertura)
    Cobertura.save()
    print("guarde")
    texto=f"Base de Coberturas de Salud familiar creado: nombre: {Cobertura.denominacion} codigo: {Cobertura.codigo}"
    print(texto)
    return HttpResponse(texto)

def familia_vinculo(request):

    Familia=familia(nombre="Ivan", apellido="Galeano", dni=92569872, extranjero="True", enfermedadbase="Locura", mail="ivangaba@gmail.com")
    Familia.save()
    texto=f"Nuevo familiar agregado: nombre: {Familia.nombre} apellido: {Familia.apellido} dni: {Familia.dni} extranjero: {Familia.extranjero} enfermedadbase: {Familia.enfermedadbase} mail: {Familia.mail}"
    return HttpResponse(texto) 

"""def Obrasocial_individuo(request):

    InfoOS=Obrasocial(nombreOS="Medife", fecha_afiliacion= 15-2-2020, plan="Oro", cargafamiliar= "ninguno")
    InfoOS.save()
    texto=f"Nueva descripcion de Obra Social: nombre: {InfoOS.nombre} fecha_afiliacion: {InfoOS.fecha} plan: {InfoOS.plan} cargafamiliar: {InfoOS.cargafamiliar}"
    return HttpResponse(texto)"""

def trabajo_titular(request):

    Trabajo=trabajo(empresa="Tecnofull", antiguedad= 20, profesion="Tecnico", contrato="Propietario")
    Trabajo.save()
    texto=f"Descripcion de trabajo agregado: empresa{Trabajo.empresa} antiguedad: {Trabajo.antiguedad} profesion: {Trabajo.profesion} contrato{Trabajo.contrato}"
    return HttpResponse(texto)

