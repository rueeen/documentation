from django.shortcuts import render
from mis_tareas.models import Listado, Tarea

l = Listado()
# Create your views here.
def home(request):
    return render(request, 'mis_tareas/home.html')

def lista_tareas(request):
    context = { 'context' : l.ordenarTareas()}
    return render(request, 'mis_tareas/tareas.html', context)

def crear_tarea(request):
    """
    It takes the data from the form, creates a new Tarea object, and then adds it to the list
    
    :param request: The request object is an HttpRequest object. It contains metadata about the request,
    including the HTTP method
    :return: The response is a string that says "Tarea agregada"
    """
    titulo = request.POST.get('titulo')
    descr = request.POST.get('descripcion')
    importancia = int(request.POST.get('importancia'))
    t = Tarea(titulo, descr, importancia)
    response = l.agregar(t)
    context = {'respuesta': response}
    return render(request, 'mis_tareas/crear.html', context)

def eliminar_tarea(request):
    titulo = request.POST.get('titulo')
    response = l.eliminar(titulo)
    context = {'respuesta': response}
    return render(request, 'mis_tareas/eliminar.html', context)