from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Establece el email como único
    contrasena = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
