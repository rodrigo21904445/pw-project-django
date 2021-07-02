from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Contacto

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'apelido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'dataNascimento': forms.DateInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nome': 'Nome',
            'apelido': 'Apelido',
            'telefone': 'Telefone',
            'email': 'Email',
            'dataNascimento': 'Data de Nascimento',
        }
