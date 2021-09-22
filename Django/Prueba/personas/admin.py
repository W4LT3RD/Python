from django.contrib import admin
from personas.models import Persona
from personas.models import domicilio

# Register your models here.
#from personas.models import Persona
#admin.site.register(Persona)
admin.site.register(domicilio)
admin.site.register(Persona)