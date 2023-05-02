from django.shortcuts import render
from django.http import HttpResponse
from TiendaOnline import settings
from gestionPedidos.models import Articulos
from django.core.mail import send_mail


# Create your views here.

def busqueda_productos(request):
    return render(request, "busqueda_productos.html")

def buscar(request):

    if request.GET["prd"]:
        #mensaje ="Articulo buscado :%r" %request.GET["prd"]
        producto  = request.GET["prd"]
        if len(producto)>20: 
            mensaje = "Texto muy largo"
        else:     
            articulos = Articulos.objects.filter (nombre__icontains = producto )
            return render(request, "resultados_busqueda.html", {"articulos":articulos, "query":producto})
    else: 
       mensaje = "Debe indicar el valor"

       
    
    return HttpResponse(mensaje)

def contacto (request):
    if request.method =="POST":
        subject = request.POST["asunto"]
        message = request.POST["mensaje"] + " " + request.POST["email"]
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["lgutiegt@gmail.com"]
        print(subject) 
        print(message)
        print(email_from) 
        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")
    
    return render(request, "contacto.html")
