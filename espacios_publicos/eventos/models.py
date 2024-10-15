from django.db import models
from espacios.models import EspacioPublico
from usuarios.models import Usuario

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    espacio = models.ForeignKey(EspacioPublico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.TextField()
    organizador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
