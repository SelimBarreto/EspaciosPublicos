from django.shortcuts import render, get_object_or_404
from .models import InstalacionDeportiva, Negocio, Partida
from django.core.serializers import serialize
from .models import EspacioPublico, Cancha

# Vista para la lista de espacios deportivos
# espacios/views.py
def lista_espacios(request):
    espacios = InstalacionDeportiva.objects.all()

    # Obtener los parámetros de los filtros
    alcaldia = request.GET.get('alcaldia')
    deporte = request.GET.get('deporte')
    acepta_mascotas = request.GET.get('acepta_mascotas')
    gratuita = request.GET.get('gratuita')
    gradas = request.GET.get('gradas')
    tipo_pasto = request.GET.get('tipo_pasto')

    # Aplicar filtros si los parámetros no están vacíos
    if alcaldia:
        espacios = espacios.filter(alcaldia__icontains=alcaldia)
    if deporte:
        espacios = espacios.filter(deporte__icontains=deporte)
    if acepta_mascotas == 'true':
        espacios = espacios.filter(acepta_mascotas=True)
    elif acepta_mascotas == 'false':
        espacios = espacios.filter(acepta_mascotas=False)
    if gratuita == 'true':
        espacios = espacios.filter(gratuita=True)
    elif gratuita == 'false':
        espacios = espacios.filter(gratuita=False)
    if gradas == 'true':
        espacios = espacios.filter(gradas=True)
    elif gradas == 'false':
        espacios = espacios.filter(gradas=False)
    if tipo_pasto:
        espacios = espacios.filter(tipo_pasto__iexact=tipo_pasto)

    contexto = {'espacios': espacios}
    return render(request, 'espacios/lista_espacios.html', contexto)

def detalle_espacio(request, id):
    espacio = get_object_or_404(InstalacionDeportiva, id=id)
    negocios = Negocio.objects.filter(espacio=espacio)
    partidas = Partida.objects.filter(espacio=espacio)
    return render(request, 'espacios/detalle_espacio.html', {'espacio': espacio, 'negocios': negocios, 'partidas': partidas})

def mapa_interactivo(request):
    # Serializa las instalaciones deportivas a GeoJSON
    instalaciones = serialize('geojson', InstalacionDeportiva.objects.all())
    return render(request, 'espacios/mapa_interactivo.html', {'instalaciones': instalaciones})