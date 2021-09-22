from django.db.models import fields
from django.forms import ModelForm, widgets
from personas.models import Persona


class PersonaForm(ModelForm):
    class Meta: 
        model = Persona
        fields = '__all__'
        widgets = {
            'email' : widgets.EmailInput(attrs={'type': 'email'})
        }