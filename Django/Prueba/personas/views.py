from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from personas.forms import PersonaForm
# Clases agregadas
from personas.models import Persona
from django.forms import modelform_factory

# Create your views here.
def bienvenida(rquest):
    return HttpResponse("Bienvenido Usuario :D")

def despedida(request):
    return HttpResponse("Adiós usario :,c")

def pag1(request):
    # return render(request, "bienvenido.html", {'msj1':'Valor mensje 1', 'msj2':'Valor mensaje 2'}) 
    # o también se puede colocar como:
    
   # mensajes = {'msj1':'Valor mensje 1', 'msj2':'Valor mensaje 2'}
   # return render(request, "bienvenido.html",mensajes

    no_personasvar = Persona.objects.count() # Cantidad de datos
    personas = Persona.objects.all() # Desplegar la información de la base de datos
    return render(request, "bienvenido.html", {'no_personas':no_personasvar, 'personas':personas})

def detallePersona(request, id):
    # persona = Persona.objects.get(pk=id) # .get para recuperar un objeto de tipo persona
    persona = get_object_or_404(Persona, pk=id) # Esto es para mostrar el error 404
    return render(request, 'personas/detalle.html', {'persona':persona})

# PersonaForm = modelform_factory(Persona, exclude=[]) # Objeto de tipo persona, agregar -> exclude[]
# Se colocó como comentario ya que se agregó el archivo *forms.py 

def nuevaPersona(request):    
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST) # Con esto se enviará desde la página al servidor 
        # Validación: 
        if formaPersona.is_valid(): # Validación de la información agregada en la pág
            formaPersona.save() # Con esto se hace un save en la base de datos 
       # else:           # *este else se colocará al final
           # return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})
            return redirect('inicio') # index = página principal
    else:
        formaPersona = PersonaForm()
        return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona}) # indica los errores dentro del formulario 
    # si el formulario no es válido se redigirá al usuario a *nuevo.html
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

def editarPersona(request):    
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save() 
            return redirect('inicio') 
    else:
        formaPersona = PersonaForm()


    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})