from django.contrib.auth.models import User
from django.db import models
from espacios.models import InstalacionDeportiva  # Importamos el modelo del espacio deportivo

class Foro(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    espacio = models.ForeignKey(InstalacionDeportiva, on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)  # Este campo guarda el creador
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Comentario(models.Model):
    foro = models.ForeignKey(Foro, related_name='comentarios', on_delete=models.CASCADE)
    contenido = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    respuesta_a = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return f'Comentario de {self.usuario} en {self.foro}'


class Reporte(models.Model):
    comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    motivo = models.TextField()
    fecha_reporte = models.DateTimeField(auto_now_add=True)
