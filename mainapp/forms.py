from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registerform(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
       data = self.cleaned_data['email']
       if User.objects.filter(email=data).exists():
           raise forms.ValidationError("El email ya está en uso")
       return data
        