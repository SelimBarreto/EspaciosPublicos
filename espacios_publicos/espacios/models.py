from django.contrib.auth.models import User
from django.contrib.gis.db import models  # Importamos directamente desde GeoDjango
from usuarios.models import Usuario


# Modelo InstalacionDeportiva
class InstalacionDeportiva(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=300)
    deporte = models.CharField(max_length=100)
    alcaldia = models.CharField(max_length=100)
    acepta_mascotas = models.BooleanField(default=False)
    gratuita = models.BooleanField(default=False)
    gradas = models.BooleanField(default=False)
    tipo_pasto = models.CharField(
        max_length=50,
        choices=[
            ('Natural', 'Natural'),
            ('Sintético', 'Sintético'),
            ('Arcilla', 'Arcilla'),
            ('No especificado', 'No especificado')
        ],
        default='No especificado'
    )
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    horario = models.CharField(max_length=100)
    servicios = models.TextField(null=True, blank=True)  # Opcional para servicios
    ubicacion = models.PointField()  # Para geolocalización

    def __str__(self):
        return f"{self.nombre} - {self.alcaldia}"

# Modelo Cancha
class Cancha(models.Model):
    etiqueta = models.CharField(max_length=100)
    deporte = models.CharField(max_length=100)  # Deporte de la cancha
    espacio = models.ForeignKey(InstalacionDeportiva, on_delete=models.CASCADE, related_name='canchas')

    def __str__(self):
        return self.etiqueta

class Negocio(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.PointField()
    espacio = models.ForeignKey(InstalacionDeportiva, on_delete=models.CASCADE)

class Partida(models.Model):
    titulo = models.CharField(max_length=100)  # Asegúrate de que este nombre es el que quieres.
    descripcion = models.TextField(default='Sin descripción')
    fecha = models.DateTimeField()
    espacio = models.ForeignKey(InstalacionDeportiva, on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario, related_name='partidas')

# Diccionario de mapeo para carga de datos
instalaciondeportiva_mapping = {
    'nombre': 'NOM_INSTA',
    'direccion': 'DIRECCION',
    'alcaldia': 'ALCALDIA',
    'ubicacion': 'geometry',
}

# Modelo EspacioPublico
class EspacioPublico(models.Model):
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=300)
    alcaldia = models.CharField(max_length=100)
    acepta_mascotas = models.BooleanField(default=False)
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    horario = models.CharField(max_length=100)
    servicios = models.TextField()
    ubicacion = models.PointField()  # Campo GIS para ubicación

    def __str__(self):
        return self.nombre
