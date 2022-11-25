from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class categoria(models.Model):
    nombre= models.CharField(max_length= 100)
    fecha_creacion= models.DateTimeField(auto_now_add= True)
    fecha_modificacion= models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return self.nombre
    class meta:
        ordering= ["-created"]

class entrada(models.Model):
    titulo= models.CharField(max_length= 120)
    imagen = models.ImageField(upload_to= "blog")
    fecha=models.DateField(auto_now_add= True)
    descripcion= RichTextField()
    autor= models.ForeignKey(User, on_delete=models.CASCADE)
    categorias= models.ManyToManyField(categoria)
    fecha_creacion= models.DateTimeField(auto_now_add= True)
    fecha_modificacion= models.DateTimeField(auto_now= True)
    def __str__(self):
        return self.titulo
    class meta:
        ordering= ["created"]