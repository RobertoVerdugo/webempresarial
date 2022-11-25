from django.shortcuts import render
from .models import entrada
# Create your views here.

def blog(request):
    entradas= entrada.objects.all()
    return render(request, 'blog/blog.html', {'entradas':entradas})

