from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import contactoform
# Create your views here.

def contacto(request):
    contacto_form= contactoform()
    if request.method == "POST":
        contacto_form= contactoform(data=request.POST)
        if contacto_form.is_valid():
            nombre= request.POST.get('nombre', '')
            correo= request.POST.get('correo', '')
            contenido= request.POST.get('contenido', '')
            return redirect (reverse('contacto') + "?ok")
    return render(request, 'contacto/contact.html', {'form':contacto_form})