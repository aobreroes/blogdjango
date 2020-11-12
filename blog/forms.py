from .models import Article, Comentarios
from django import forms
from django.core import validators

class CommentForm(forms.Form):

    contenido = forms.CharField(
        
        label="",
        max_length=255,
        required=True,
        widget=forms.Textarea(attrs={'rows':10, 'cols':122,'style':'padding:7px'}),
        validators=[
            validators.MinLengthValidator(10, 'El contenido es demasiado corto'),
        ] 
        
        )

    contenido.widget.attrs.update({'placeholder':'Introduce tu comentario'})


