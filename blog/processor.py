from blog.models import Category, Article, Comentarios
from django.shortcuts import render, redirect
from .forms import CommentForm



def get_categorie(request):

    categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    categories = Category.objects.filter(id__in=categories_in_use).all()

    return {

        'categories': categories,

    }

def get_article(request):

    articles = Article.objects.filter(public=True).all()

    return {

        'articles': articles

    }

def get_article_lateral(request):

    articles = Article.objects.filter(public=True).all()

    return {

        'articles2': articles

    }

def get_comments(request):

    comments = Comentarios.objects.filter(public=True).all()
    

    return {

        'comments': comments


    }



