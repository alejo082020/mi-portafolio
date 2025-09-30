from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=300)
    descripcion = models.TextField()
    palabras_clave = models.CharField(max_length=200, blank=True)
    imagen = models.ImageField(upload_to="recetas/", blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
