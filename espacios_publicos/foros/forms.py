from .models import Foro
from django import forms
from .models import Comentario

class ForoForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['titulo', 'descripcion', 'creador']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 4, 'cols': 50}),
            'creador': forms.TextInput(attrs={'placeholder': 'Tu nombre o alias'}),
        }




class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí...'})
        }
