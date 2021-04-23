from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return render(request, 'proyectowebapp/inicio.html')

def servicios(request):
    return render(request, 'proyectowebapp/servicios.html')
    
def tienda(request):
    return render(request, 'proyectowebapp/tienda.html')

def blog(request): 
    return render(request, 'proyectowebapp/blog.html')

def contacto(request): 
    return render(request, 'proyectowebapp/contacto.html')

