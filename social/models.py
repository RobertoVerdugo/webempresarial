from django.db import models

# Create your models here.
class Enlace(models.Model):
    clave= models.SlugField(max_length= 120, unique= True)
    nombre= models.CharField(max_length= 120)
    url= models.URLField(max_length= 200, null=True, blank=True)
    fecha_creacion= models.DateTimeField(auto_now_add= True)
    fecha_modificacion= models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.nombre
    class meta:
        ordering= ["-created"]