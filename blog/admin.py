from django.contrib import admin
from .models import Category, Article, Comentarios

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_filter = ('public', 'user__username', 'categories__name')
    list_display = ('title', 'public', 'user', 'created_at')
    ordering = ('-created_at',)

    #para guardar articulo con el usuario registrado actualmente sin seleccionar de manera manual
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()



class commentAdmin(admin.ModelAdmin):
    readonly_fields = ('autor_id', 'created_date')
    search_fields = ('autor_id', 'content', 'article_id')
    list_filter = ('public', 'autor_id', 'article_id')
    list_display = ('content', 'public', 'created_date')
    ordering = ('-created_date',)
    



admin.site.register(Comentarios, commentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)



