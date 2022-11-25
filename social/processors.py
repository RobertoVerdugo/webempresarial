from .models import Enlace

def contexto(request):
    ctx={'test':'hola'}
    enlaces = Enlace.objects.all()
    for enlace in enlaces:
        ctx[enlace.clave]= enlace.url
    return ctx
