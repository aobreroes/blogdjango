from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Category, Article, Comentarios
from django.core.paginator import Paginator #Paginacion
from django.contrib import messages
from .forms import CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):

    articles = Article.objects.filter(public=True)
    paginator = Paginator(articles, 4)

    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'articles/articles.html',{

        'title': 'Bienvenido al Blog con Django',
        'articles': page_articles


    })


def listcategories(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(categories=category)
    paginator = Paginator(articles, 4)

    page = request.GET.get('page')
    page_articles = paginator.get_page(page)

    return render(request, 'categories/categories.html',{

        'categorieslist': category,
        'articles': page_articles


    })

def view_article(request, article_id):

    article = get_object_or_404(Article, id=article_id)
    num_comentarios = Comentarios.objects.filter(article_id=article_id).all()


    return render(request, 'articles/view.html',{

        'article': article,
        'numcomments': num_comentarios


    })

@login_required(login_url="login")
def add_comment(request, article_id):

    register_form = CommentForm()

    if request.method == 'POST':

        register_form = CommentForm(request.POST)

        if register_form.is_valid():


            datos_form = register_form.cleaned_data

            article_id = article_id
            content = datos_form.get('contenido')
            autor = request.user.id

            comment = Comentarios(
                
            article_id = article_id,
            content = content,
            autor_id = autor

            )

            comment.save()

            return redirect('articulo', article_id)

    return render(request, 'articles/insert_comment.html',{

        'form': register_form

    })






