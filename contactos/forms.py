from django.forms import ModelForm
from .models import Contactos

class ContactosForm(ModelForm):
    class Meta:
        model = Contactos
        fields = ['nome', 'sobrenome', 'contacto', 'foto', 'email', 'morada', 'grupo', 'notas']