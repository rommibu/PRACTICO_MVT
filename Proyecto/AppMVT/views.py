from django.http import HttpResponse
from django.shortcuts import render
from .models import Coberturasalud, familia, trabajo
from AppMVT.forms import FormularioFamilia
import datetime

def inicio(request):
    return render (request, "AppMVT/inicio.html")

def conocenos(request):
    return render (request, "AppMVT/conocenos.html")

def prestadores(request):
    return render (request, "AppMVT/prestadores.html")

def quienes_somos(request):
    return render(request, "AppMVT/quienes_somos.html")

def leyes(request):
    return render (request, "AppMVT/leyes.html")

def Cobertura_salud(request):
    return render(request, "AppMVT/cobertura.html")
    #Cobertura1=Coberturasalud(denominacion="Medife", codigo=3624, fecha_afiliacion="2020-2-20")
    #Cobertura1.save()
    #Cobertura2=Coberturasalud(denominacion="Swiss_Medical", codigo=3782, fecha_afiliacion="2018-11-22")
    #Cobertura2.save()
    #Cobertura3=Coberturasalud(denominacion="Pami", codigo=1436, fecha_afiliacion="2007-5-11")
    #Cobertura3.save()
    #Cobertura4=Coberturasalud(denominacion="Apross", codigo=41325, fecha_afiliacion="2022-2-18")
    #Cobertura4.save()
    #lista=[Cobertura1, Cobertura2, Cobertura3, Cobertura4]
    #return render(request, "AppMVT/cobertura.html", {"listado":lista})



    #Cobertura=Coberturasalud(denominacion="Medife", codigo=3624, fecha_afiliacion="2020-2-20") 
    #Cobertura.save()
    #texto=f"Base de Coberturas de Salud familiar creado: nombre: {Cobertura.denominacion} codigo: {Cobertura.codigo}"
    #return HttpResponse(texto)
    
def familia_vinculo(request):
    #return render(request, "AppMVT/familia.html")
    Familia=familia(nombre="Ivan", apellido="Galeano", dni=92569872, extranjero="True", enfermedadbase="Locura", mail="ivangaba@gmail.com")
    Familia.save()
    texto=f"Nuevo familiar agregado: nombre: {familia.nombre} apellido: {familia.apellido} dni: {familia.dni} extranjero: {familia.extranjero} enfermedadbase: {familia.enfermedadbase} mail: {familia.mail}"
    return HttpResponse(texto)


def trabajo_titular(request):
    return render(request, "AppMVT/trabajo.html")
    #Trabajo=trabajo(empresa="Tecnofull", antiguedad= 20, profesion="Tecnico", contrato="Propietario")
    #Trabajo.save()
    #texto=f"Descripcion de trabajo agregado: empresa{Trabajo.empresa} antiguedad: {Trabajo.antiguedad} profesion: {Trabajo.profesion} contrato{Trabajo.contrato}"
    #return HttpResponse(texto)

def formularioFamilia(request):
    
    if request.method=="POST":
       miFormulario=formularioFamilia(request.POST)
       print(miFormulario)
       if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            print(info)
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            dni=info.get("dni")
            extranjero=info.get("extranjero")
            enfermedadbase=info.get("enfermedad_base")
            mail=info.get("mail")
            Familia=familia(nombre=nombre, apellido=apellido, dni=dni, extranjero=extranjero, enfermedadbase=enfermedadbase, mail=mail)
            Familia.save()
            return render(request, "AppMVT/inicio.html", {"mensaje": "Tu informacion quedo registrada!"})
       else:
            return render(request, "AppMVT/inicio.html", {"mensaje": "Ingreso algun dato incorrecto, por favor verifique!"})
    else:
        miFormulario=FormularioFamilia()
        return render(request, "AppMVT/formularioFamilia.html", {"formulario":miFormulario})
        
#def busquedaFamilia (request):
#    return render(request, "AppMVT/busquedaFamilia.html")

#def buscar(request):
#    dni=request.GET.get("dni")
#    return HttpResponse(f"Busqueda de DNI {dni}")




"""View para formulario a mano
def formulario(request):
    if request.method=="POST":
        nombre=request.POST.get("nombre")
        apellido=request.POST.get("apellido")
        dni=request.POST.get("edad")
        extranjero=request.POST.get("extranjero")
        enfermedadbase=request.POST.get("enfermedad_base")
        mail=request.POST.get("mail")
        familia_vinculo=familia(nombre=nombre, apellido=apellido, dni=dni, extranjero=extranjero, enfermedadbase=enfermedadbase, mail=mail)
        familia_vinculo.save()
        return render(request, "AppMVT/inicio.html")
    return render(request, "AppMVT/formulario.html")"""
