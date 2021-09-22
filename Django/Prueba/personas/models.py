from django.db import models

# Create your models here.
class domicilio(models.Model):
    calle = models.CharField(max_length=255)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=255)

    def __str__(self):
        return f'Domicilio {self.id}: {self.calle} {self.no_calle} {self.pais}'

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    #atributo, se coloca como nulo si se elimina alguna parte de domicilio
    domicilio = models.ForeignKey(domicilio, on_delete=models.SET_NULL, null=True) 
    # models.Set_NULL hace que se coloque como nulo
    # Si se utiliza models.CASCADE, se eliminará el registro persona con el que está relacionado
    
    
    
    def __str__(self): #Aqui se modifica para mostrar de mejor manera la información de las personas
        return f'Persona {self.id} : {self.nombre} {self.apellido}, {self.email}' 