from django.contrib import admin

from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    """docstring for ."""
    readonly_fields = ['created', 'updated',]
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    ordering = ['-created']

class PostAdmin(admin.ModelAdmin):
    """docstring for PostAdmin."""
    readonly_fields = ['created', 'updated',]
    verbose_name = 'entrada'
    verbose_name_plural = 'entradas'
    ordering = ('author', 'published')
    list_display = ('title', 'author', 'published', 'post_categories')
    search_fields = ('content', 'title', 'author__username', 'categories__name')
    date_hierarchy = ('published')
    list_filter = ['author__username', 'categories__name']

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
