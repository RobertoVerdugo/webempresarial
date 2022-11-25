from django.shortcuts import render
from .models import servicio
# Create your views here.

def servicios(request):
    servicios = servicio.objects.all()
    return render(request, 'servicios/services.html', {'servicios':servicios})