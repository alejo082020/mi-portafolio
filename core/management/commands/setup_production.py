"""
Comando personalizado para configurar datos iniciales en producción
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Perfil, Skill, Proyecto, Banner
from faq.models import Pregunta
from open.models import Receta
from datetime import date

User = get_user_model()

class Command(BaseCommand):
    help = 'Configura datos iniciales para producción'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Configurando datos iniciales...\n')
        
        # 1. Crear superusuario
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@portafolio.com',
                password='admin123'
            )
            self.stdout.write(self.style.SUCCESS('✅ Superusuario creado'))
        else:
            self.stdout.write('⏭️  Superusuario ya existe')
        
        # 2. Crear perfil
        perfil, created = Perfil.objects.get_or_create(
            id=1,
            defaults={
                'nombre_completo': 'Edin Alejandro Alvarez Laverde',
                'titulo_profesional': 'Estudiante de Ingeniería de Software',
                'descripcion': 'Estudiante de Ingeniería de Software en proceso de aprendizaje, apasionado por el desarrollo web y las nuevas tecnologías. Me encuentro desarrollando habilidades en Django, Python y JavaScript mientras construyo proyectos prácticos para fortalecer mi experiencia.',
                'email': 'edin.alvarez@ejemplo.com',
                'telefono': '+57 300 123 4567',
                'linkedin': 'https://linkedin.com/in/edin-alvarez',
                'github': 'https://github.com/edin-alvarez'
            }
        )
        self.stdout.write(self.style.SUCCESS(f'✅ Perfil: {perfil.nombre_completo}'))
        
        # 3. Crear skills
        skills_data = [
            ('HTML5', 90, 1), ('CSS3', 85, 2), ('JavaScript', 80, 3),
            ('Python', 85, 4), ('Django', 75, 5), ('Bootstrap', 80, 6),
        ]
        for nombre, nivel, orden in skills_data:
            Skill.objects.get_or_create(nombre=nombre, defaults={'nivel': nivel, 'orden': orden})
        self.stdout.write(self.style.SUCCESS(f'✅ Skills creados'))
        
        # 4. Crear proyectos
        if not Proyecto.objects.exists():
            Proyecto.objects.create(
                titulo='Portafolio Personal',
                descripcion='Sitio web de portafolio personal desarrollado con Django',
                tecnologias='Django, Python, JavaScript, Bootstrap',
                fecha=date.today(),
                destacado=True
            )
            self.stdout.write(self.style.SUCCESS('✅ Proyectos creados'))
        
        # 5. Crear banners
        Banner.objects.update_or_create(
            titulo='NICOLAS PARRA',
            defaults={
                'url': 'https://cv-nicolas-torres.up.railway.app',
                'utm_source': 'friend',
                'utm_medium': 'referral',
                'utm_campaign': 'friend_referral',
                'activo': True,
                'orden': 1
            }
        )
        Banner.objects.update_or_create(
            titulo='DIEGO ROJAS MARTINEZ',
            defaults={
                'url': 'https://cvdiego.up.railway.app',
                'utm_source': 'friend',
                'utm_medium': 'referral',
                'utm_campaign': 'friend_referral',
                'activo': True,
                'orden': 2
            }
        )
        self.stdout.write(self.style.SUCCESS('✅ Banners creados'))
        
        # 6. Crear preguntas frecuentes
        preguntas_data = [
            {
                'titulo': '¿Qué tecnologías estás aprendiendo?',
                'respuesta': 'Actualmente estoy aprendiendo Python y Django para el backend, JavaScript para el frontend, y bases de datos como PostgreSQL y SQLite. También estoy familiarizándome con frameworks CSS como Bootstrap.'
            },
            {
                'titulo': '¿Cuánto tiempo llevas estudiando programación?',
                'respuesta': 'Estoy en proceso de formación en Ingeniería de Software, aprendiendo y practicando constantemente. Me especializo en desarrollo web con Django y estoy construyendo proyectos para ganar experiencia práctica.'
            },
            {
                'titulo': '¿Estás disponible para colaborar en proyectos?',
                'respuesta': 'Sí, estoy abierto a colaborar en proyectos educativos y de código abierto. Es una excelente manera de aprender y mejorar mis habilidades mientras contribuyo a la comunidad.'
            },
            {
                'titulo': '¿Cómo puedo contactarte?',
                'respuesta': 'Puedes contactarme a través del formulario de contacto en este sitio, por email, o a través de mis redes sociales (LinkedIn, GitHub). Respondo generalmente en menos de 24 horas.'
            },
        ]
        for pregunta_data in preguntas_data:
            Pregunta.objects.get_or_create(
                titulo=pregunta_data['titulo'],
                defaults={'respuesta': pregunta_data['respuesta']}
            )
        self.stdout.write(self.style.SUCCESS('✅ Preguntas frecuentes creadas'))
        
        # 7. Crear recetas
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
            Receta.objects.get_or_create(
                titulo=receta_data['titulo'],
                defaults=receta_data
            )
        self.stdout.write(self.style.SUCCESS('✅ Recetas creadas'))
        
        self.stdout.write(self.style.SUCCESS('\n🎉 ¡Configuración completada!'))
