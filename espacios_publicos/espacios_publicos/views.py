from django.shortcuts import render


def index(request):
    return render(request, 'espacios_publicos/index.html')  # Ruta correcta
