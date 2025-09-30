from django.contrib import admin
from .models import Contacto, Perfil, Skill, Proyecto, Banner

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ['nombre_completo', 'email']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nivel', 'orden']
    list_editable = ['orden']

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'fecha', 'destacado']
    list_filter = ['destacado', 'fecha']
    list_editable = ['destacado']

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'utm_campaign', 'activo', 'orden']
    list_editable = ['activo', 'orden']

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'correo', 'asunto', 'fecha_envio', 'leido']
    list_filter = ['leido', 'fecha_envio']
    list_editable = ['leido']
    readonly_fields = ['fecha_envio']
