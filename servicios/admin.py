from django.contrib import admin
from .models import servicio

# Register your models here.
class servicio_admin(admin.ModelAdmin):
    readonly_fields = ('fecha_creacion','fecha_modificacion')


admin.site.register(servicio, servicio_admin)
