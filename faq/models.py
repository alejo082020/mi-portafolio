from django.db import models

class Pregunta(models.Model):
    titulo = models.CharField(max_length=255)
    respuesta = models.TextField()

    def __str__(self):
        return self.titulo