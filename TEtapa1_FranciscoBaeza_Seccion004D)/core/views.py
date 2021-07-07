from django.shortcuts import render, redirect
from .models import datos, publicacion
from .forms import datosForm, publicacionForm


# Create your views here.
def home(request):
    nombre = 'Francisco Baeza'

    datosForm = datos.objects.all()    #es similar al comando select de consultas 

    return render(request, 'home.html', context={'nombre_usuario':nombre,'datos':datos})

def form_datos(request):
    if request.method == 'POST': 
        datos_form = datosForm(request.POST)
        if datos_form.is_valid():
            datos_form.save()        #similar al insert de un modelo relacional 
            return redirect('home')
    else: 
        datos_form = datosForm()
    return render(request, 'core/form_crear.html', {'datos_form': datos_form})

def Ver(request):
    datosForm = datos.objects.all()

    return render(request, 'core/ver.html', {'datos': datosForm})

def form_modificar(request, id):
    datosForm = datos.objects.get(rutcola=id)

    datos ={
        'form': datosForm(instance=datos)
    }
    if request.method == 'POST': 
        formulario = datosForm(data=request.POST, instance = datos)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_modificar.html', datos)

def form_eliminacion(request,id):
    datosForm = datos.objects.get(rutcola=id)
    datos.delete()
    return redirect('ver')

def form_publicacion(request):
    if request.method == 'POST': 
        publicacion_form = publicacionForm(request.POST)
        if publicacion_form.is_valid():
            publicacion_form.save()        #similar al insert de un modelo relacional 
            return redirect('home')
    else: 
        publicacion_form = publicacionForm()
    return render(request, 'core/form_publicacion.html', {'publicacion_form': publicacion_form})