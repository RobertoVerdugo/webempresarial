from django.contrib import admin
from .models import entrada, categoria
# Register your models here.
class entrada_admin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion','fecha_modificacion')
    list_display=('titulo', 'autor', 'fecha_creacion')
    search_fields=('titulo', 'autor__username', 'categorias__nombre')
class categoria_admin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion','fecha_modificacion')

admin.site.register(entrada, entrada_admin)
admin.site.register(categoria, categoria_admin)