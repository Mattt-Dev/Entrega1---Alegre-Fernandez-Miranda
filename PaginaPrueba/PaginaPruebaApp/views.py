from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def inicio(request):
    cursos = Curso.objects.all()
    cursos = cursos[len(cursos)-3:len(cursos)]
    eventos = Evento.objects.all()
    eventos = eventos[len(eventos)-3:len(eventos)]  

    return render(request, "PaginaPruebaApp/index.html", {"cursos":cursos , "eventos":eventos})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "PaginaPruebaApp/cursos.html", {"cursos":cursos})

def eventos(request):
    eventos = Evento.objects.all()
    return render(request, "PaginaPruebaApp/eventos.html", {"eventos":eventos})

def formulario(request):
    return render(request, "PaginaPruebaApp/formulario.html", {})

def crear_formulario_curso(request):

    if request.method == "POST":
        formulario = crear_formulario_Curso(request.POST)
        print(formulario)

        if formulario.is_valid():
            informacion = formulario.cleaned_data

            curso = Curso(nombre=informacion['curso'], fecha_inicio=informacion['fecha_inicio'], profesor=informacion['profesor'], comision=informacion['comision'])

            curso.save()

            return redirect('inicio')
            
        
    else:

        formulario = crear_formulario_Curso()

        return render(request, "PaginaPruebaApp/formulario_cursos.html", {"formulario":formulario})

def crear_formulario_evento(request):

    if request.method == "POST":
        formulario = crear_formulario_Evento(request.POST)
        print(formulario)

        if formulario.is_valid():
            informacion = formulario.cleaned_data

            evento = Evento(nombre_evento=informacion['nombre_evento'], fecha_inicio=informacion['fecha_inicio'], disertante=informacion['disertante'])

            evento.save()

            return redirect('inicio')

        
    else:

        formulario = crear_formulario_Evento()

        return render(request, "PaginaPruebaApp/formulario_eventos.html", {"formulario":formulario})

def crear_formulario_nosotros(request):

    if request.method == "POST":
        formulario = crear_formulario_Nosotros(request.POST)
        print(formulario)

        if formulario.is_valid():
            informacion = formulario.cleaned_data

            curso = Nosotros(nombre=informacion['nombre'], fecha_nacimiento=informacion['fecha_nacimiento'], estudios=informacion['estudios'], acerca_de=informacion['acerca_de'])

            curso.save()

            return redirect('inicio')
        
    else:

        formulario = crear_formulario_Nosotros()

        return render(request, "PaginaPruebaApp/formulario_nosotros.html", {"formulario":formulario})


def busqueda_curso(request):
    return render(request, "PaginaPruebaApp/busqueda_curso.html")

def buscar(request):
    if request.GET["nombre"]:

        nombre = request.GET['nombre']
        cursos = Curso.objects.filter(nombre__icontains=nombre)

        return render(request,"PaginaPruebaApp/resultado_busqueda.html", {"cursos":cursos, "nombre":nombre})
    
    else:

        return HttpResponse("No se ingresaron datos correctos.")

    



