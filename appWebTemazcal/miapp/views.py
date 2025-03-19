from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request,'index.html')

def pagina_servicios(request):
  return render(request,'servicios.html')

def pagina_conocenos(request):
  return render(request,'conocenos.html')

def pagina_reservaciones(request):
  return render(request,'reservaciones.html')

def pagina_ubicacion(request):
  return render(request,'ubicacion.html')
