from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #formularios para usuarios
from .forms import Registerform #importando el formulario con los campos desde form
from django.contrib import messages #mensajes flash
from django.contrib.auth import authenticate, login, logout #para login de usuarios
from blog.models import Article
from django.core.paginator import Paginator 
from django.db.models import Q


# Create your views here.


def index(request):

    articles_search=""

    if request.method == 'POST':

        search = request.POST.get('search')
        articles_search = Article.objects.filter(Q(title__icontains=search) | Q(content__icontains=search))

        if not articles_search:

            errorbusqueda = messages.info(request, "No hay resultados con esa busqueda")

    return render(request, 'mainapp/index.html', {
    
    'title': 'Bienvenido al Sitio Web con Django',
    'articles_search': articles_search

    
    })

def register_page(request):
    
    if request.user.is_authenticated:
        return redirect('index')
    
    else:

        register_form = Registerform()

        if request.method == 'POST':
            register_form = Registerform(request.POST)

            if register_form.is_valid():

                register_form.save()

                messages.success(request, "Te has registrado correctamente")

                return redirect('login')

        return render(request, 'users/register.html',{

            'title': 'Registro',
            'register_form': register_form

        })

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.warning(request, "Error en el inicio de sesión. Comprueba el usuario y contraseña")

    return render(request, 'users/login.html',{

        'title': 'Login'
    })
    
def logout_user(request):

    logout(request)
    return redirect('login')
