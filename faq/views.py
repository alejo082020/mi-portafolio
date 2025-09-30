from django.shortcuts import render
from .models import Pregunta

def faq_list(request):
    """Vista de preguntas frecuentes gestionadas desde CMS"""
    preguntas = Pregunta.objects.all()
    return render(request, "fyq.html", {"preguntas": preguntas})
