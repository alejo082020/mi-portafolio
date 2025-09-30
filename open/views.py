from django.shortcuts import render, get_object_or_404
from .models import Receta

def open_list(request):
    """Vista en grid de recetas gestionadas desde CMS"""
    recetas = Receta.objects.all().order_by('-fecha_creacion')
    return render(request, "open.html", {"recetas": recetas})

def open_detail(request, pk):
    """Vista de detalle de una receta"""
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, "open_detail.html", {"receta": receta})
