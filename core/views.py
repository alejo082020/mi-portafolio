from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactoForm
from .models import Perfil, Skill, Proyecto, Banner

def home(request):
    """Vista principal con hoja de vida y portafolio"""
    perfil = Perfil.objects.first()  # Obtener el perfil del CMS
    skills = Skill.objects.all()
    proyectos = Proyecto.objects.filter(destacado=True)[:6]
    banners = Banner.objects.filter(activo=True)
    
    context = {
        'perfil': perfil,
        'skills': skills,
        'proyectos': proyectos,
        'banners': banners
    }
    return render(request, "home.html", context)

def contactame(request):
    """Vista del formulario de contacto con validación"""
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por contactarme! Te responderé pronto.')
            return redirect('contacto_exitoso')
    else:
        form = ContactoForm()
    return render(request, "contactame.html", {"form": form})

def contacto_exitoso(request):
    """Página de confirmación después de enviar el formulario"""
    return render(request, "contacto_exitoso.html")

def test_analytics(request):
    """Página de prueba para Google Analytics"""
    return render(request, "test_analytics.html")
