from django import forms
from .models import Contatto
from django.core.exceptions import ValidationError

class FormContatto(forms.ModelForm):
    class Meta:
        model = Contatto
        fields = "__all__"
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class':'form-control'}),
            'cognome': forms.TextInput(attrs={'placeholder': 'Compila questo campo', 'class':'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Compila questo campo', 'class':'form-control'}),
            'contenuto': forms.Textarea(attrs={'placeholder': 'Compila questo campo', 'class':'form-control'}),
        }

    def clean_contenuto(self):
        dati=self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viola le norme del sito!")
        if len(dati)<20:
            raise ValidationError("Il contenuto inserito è troppo breve")
        return dati