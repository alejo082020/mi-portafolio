"""
Comando personalizado para configurar datos iniciales en producción
"""
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from core.models import Perfil, Skill, Proyecto, Banner
from faq.models import Pregunta
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
                'titulo_profesional': 'Desarrollador Web Full Stack',
                'descripcion': 'Estudiante de Ingeniería Web apasionado por crear experiencias digitales increíbles.',
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
        self.stdout.write(self.style.SUCCESS('✅ Banners creados'))
        
        self.stdout.write(self.style.SUCCESS('\n🎉 ¡Configuración completada!'))
