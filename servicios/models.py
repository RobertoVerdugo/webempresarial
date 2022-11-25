from django.db import models

# Create your models here.

class servicio(models.Model):
    titulo= models.CharField(max_length= 120)
    sub_titulo= models.CharField(max_length= 120)
    imagen = models.ImageField(upload_to= "servicios")
    descripcion= models.TextField()
    fecha_creacion= models.DateTimeField(auto_now_add= True)
    fecha_modificacion= models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.titulo
    class meta:
        ordering= ["-created"]
