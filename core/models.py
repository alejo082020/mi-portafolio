"""
Modelos para el portafolio
"""

from django.db import models

class Perfil(models.Model):
    """Modelo para gestionar la información del portafolio desde el CMS"""
    nombre_completo = models.CharField(max_length=200)
    titulo_profesional = models.CharField(max_length=200)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to="perfil/", blank=True, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Perfil"
    
    def __str__(self):
        return self.nombre_completo

class Skill(models.Model):
    """Habilidades técnicas"""
    nombre = models.CharField(max_length=100)
    nivel = models.IntegerField(default=50, help_text="Nivel de 0 a 100")
    orden = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
    
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    """Proyectos del portafolio"""
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="proyectos/", blank=True, null=True)
    url = models.URLField(blank=True)
    tecnologias = models.CharField(max_length=200, help_text="Separadas por comas")
    fecha = models.DateField()
    destacado = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return self.titulo

class Banner(models.Model):
    """Banners con UTM para rastreo"""
    titulo = models.CharField(max_length=200)
    url = models.URLField()
    utm_source = models.CharField(max_length=100)
    utm_medium = models.CharField(max_length=100)
    utm_campaign = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)
    orden = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
    
    def get_url_completa(self):
        return f"{self.url}?utm_source={self.utm_source}&utm_medium={self.utm_medium}&utm_campaign={self.utm_campaign}"
    
    def __str__(self):
        return self.titulo

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    correo = models.EmailField(verbose_name="Correo electrónico")
    telefono = models.CharField(max_length=20, blank=True, default='', verbose_name="Teléfono")
    asunto = models.CharField(max_length=200, default='Consulta general', verbose_name="Asunto")
    mensaje = models.TextField(verbose_name="Mensaje")
    fecha_envio = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-fecha_envio']
        verbose_name_plural = "Contactos"
    
    def __str__(self):
        return f"{self.nombre} - {self.asunto}"