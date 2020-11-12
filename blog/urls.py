from django.urls import path
from . import views

urlpatterns=[

    path('articulos/', views.articles, name="blog"),
    path('categorias/<int:category_id>', views.listcategories, name="categorias"),
    path('articulo/<int:article_id>', views.view_article, name="articulo"),
    path('insertcomment/<int:article_id>', views.add_comment, name="comment")
]