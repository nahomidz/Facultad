from django import forms 
from django.forms import fields
from .models import registro

class comentario(forms.ModelForm):
    class Meta:
        model = registro
        fields = '__all__'
        

    