"""
Script para agregar datos básicos al portafolio
Ejecutar: python agregar_datos_basicos.py
"""

import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_portafolio.settings')
django.setup()

from core.models import Perfil, Skill, Proyecto
from faq.models import Pregunta
from open.models import Receta

print("🚀 Agregando datos básicos al portafolio...\n")

# 1. Perfil
print("📝 Creando perfil...")
perfil, created = Perfil.objects.get_or_create(
    id=1,
    defaults={
        'nombre_completo': 'Edin Alejandro Alvarez Laverde',
        'titulo_profesional': 'Desarrollador Web Full Stack',
        'descripcion': 'Estudiante de Ingeniería Web apasionado por crear experiencias digitales increíbles. Con conocimientos en Django, Python, JavaScript y tecnologías modernas de desarrollo web.',
        'email': 'edin.alvarez@ejemplo.com',
        'telefono': '+57 300 123 4567',
        'linkedin': 'https://linkedin.com/in/edin-alvarez',
        'github': 'https://github.com/edin-alvarez'
    }
)
print(f"  {'✅ Creado' if created else '⏭️  Ya existe'}: {perfil.nombre_completo}\n")

# 2. Skills
print("🎯 Creando skills...")
skills_data = [
    ('HTML5', 90, 1),
    ('CSS3', 85, 2),
    ('JavaScript', 80, 3),
    ('Python', 85, 4),
    ('Django', 75, 5),
    ('Bootstrap', 80, 6),
    ('Git', 70, 7),
    ('SQL', 75, 8),
]

for nombre, nivel, orden in skills_data:
    skill, created = Skill.objects.get_or_create(
        nombre=nombre,
        defaults={'nivel': nivel, 'orden': orden}
    )
    print(f"  {'✅' if created else '⏭️ '} {nombre}")

# 3. Proyectos
print("\n💼 Creando proyectos...")
proyectos_data = [
    {
        'titulo': 'Portafolio Personal',
        'descripcion': 'Sitio web de portafolio personal desarrollado con Django, incluyendo sistema de gestión de contenidos, formulario de contacto con validación JavaScript, y integración con Google Analytics.',
        'tecnologias': 'Django, Python, JavaScript, Bootstrap, Google Analytics',
        'fecha': date(2025, 9, 29),
        'destacado': True,
        'url': 'https://github.com/edin-alvarez/portafolio'
    },
    {
        'titulo': 'Sistema de Gestión Escolar',
        'descripcion': 'Plataforma web para gestión de estudiantes, profesores y calificaciones. Incluye panel de administración y reportes.',
        'tecnologias': 'Django, PostgreSQL, Bootstrap',
        'fecha': date(2025, 6, 15),
        'destacado': True,
        'url': ''
    },
    {
        'titulo': 'Blog con CMS',
        'descripcion': 'Blog personal con sistema de gestión de contenidos, comentarios y categorías.',
        'tecnologias': 'Django, SQLite, Markdown',
        'fecha': date(2025, 3, 10),
        'destacado': True,
        'url': ''
    },
]

for proyecto_data in proyectos_data:
    proyecto, created = Proyecto.objects.get_or_create(
        titulo=proyecto_data['titulo'],
        defaults=proyecto_data
    )
    print(f"  {'✅' if created else '⏭️ '} {proyecto_data['titulo']}")

# 4. Preguntas Frecuentes
print("\n❓ Creando preguntas frecuentes...")
preguntas_data = [
    {
        'titulo': '¿Qué tecnologías utilizas?',
        'respuesta': 'Trabajo principalmente con Python y Django para el backend, JavaScript para el frontend, y bases de datos como PostgreSQL y SQLite. También tengo experiencia con frameworks CSS como Bootstrap.'
    },
    {
        'titulo': '¿Cuánto tiempo llevas programando?',
        'respuesta': 'Estoy en proceso de formación en Ingeniería Web, aprendiendo y practicando constantemente. Me especializo en desarrollo web con Django.'
    },
    {
        'titulo': '¿Trabajas de forma remota?',
        'respuesta': 'Sí, tengo experiencia trabajando de forma remota y cuento con las herramientas necesarias para colaborar efectivamente en proyectos.'
    },
    {
        'titulo': '¿Cómo puedo contactarte?',
        'respuesta': 'Puedes contactarme a través del formulario de contacto en este sitio, por email, o a través de mis redes sociales (LinkedIn, GitHub). Respondo generalmente en menos de 24 horas.'
    },
    {
        'titulo': '¿Qué tipo de proyectos te interesan?',
        'respuesta': 'Me interesan proyectos de desarrollo web, especialmente aquellos que involucren Django, Python y tecnologías modernas. Estoy abierto a colaborar en proyectos educativos y de código abierto.'
    },
]

for pregunta_data in preguntas_data:
    pregunta, created = Pregunta.objects.get_or_create(
        titulo=pregunta_data['titulo'],
        defaults={'respuesta': pregunta_data['respuesta']}
    )
    print(f"  {'✅' if created else '⏭️ '} {pregunta_data['titulo'][:50]}...")

# 5. Recetas
print("\n🍳 Creando recetas de ejemplo...")
recetas_data = [
    {
        'titulo': 'Pasta Carbonara Clásica',
        'resumen': 'Deliciosa pasta italiana con huevo, queso y panceta',
        'descripcion': 'Ingredientes:\n- 400g de pasta\n- 200g de panceta\n- 4 huevos\n- 100g de queso parmesano\n- Sal y pimienta\n\nPreparación:\n1. Cocina la pasta según las instrucciones.\n2. Fríe la panceta hasta que esté crujiente.\n3. Mezcla huevos con queso.\n4. Combina todo y sirve caliente.',
        'palabras_clave': 'pasta, italiana, carbonara, fácil',
    },
    {
        'titulo': 'Ensalada César',
        'resumen': 'Ensalada fresca con pollo y aderezo césar',
        'descripcion': 'Ingredientes:\n- Lechuga romana\n- Pechuga de pollo\n- Queso parmesano\n- Crutones\n- Aderezo césar\n\nPreparación:\n1. Cocina el pollo a la plancha.\n2. Corta la lechuga.\n3. Mezcla con aderezo.\n4. Agrega crutones y queso.',
        'palabras_clave': 'ensalada, saludable, pollo',
    },
    {
        'titulo': 'Tacos al Pastor',
        'resumen': 'Tacos mexicanos con carne marinada',
        'descripcion': 'Ingredientes:\n- 500g de carne de cerdo\n- Tortillas\n- Piña\n- Cebolla y cilantro\n- Especias mexicanas\n\nPreparación:\n1. Marina la carne con especias.\n2. Cocina en plancha.\n3. Sirve en tortillas con piña y cilantro.',
        'palabras_clave': 'mexicana, tacos, picante',
    },
]

for receta_data in recetas_data:
    receta, created = Receta.objects.get_or_create(
        titulo=receta_data['titulo'],
        defaults=receta_data
    )
    print(f"  {'✅' if created else '⏭️ '} {receta_data['titulo']}")

print("\n" + "="*60)
print("✅ ¡Datos básicos agregados exitosamente!")
print("="*60)
print("\n📊 Resumen:")
print(f"  - Perfiles: {Perfil.objects.count()}")
print(f"  - Skills: {Skill.objects.count()}")
print(f"  - Proyectos: {Proyecto.objects.count()}")
print(f"  - Preguntas: {Pregunta.objects.count()}")
print(f"  - Recetas: {Receta.objects.count()}")
print("\n🌐 Tu sitio está listo en: http://127.0.0.1:8080/")
print("🔧 Panel admin: http://127.0.0.1:8080/admin/")
print("\n💡 Puedes editar todo desde el panel de administración")
