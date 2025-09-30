"""
Script para poblar la base de datos con datos de ejemplo.
SOLO PARA DESARROLLO Y PRUEBAS.

Uso:
    python manage.py shell < poblar_datos_ejemplo.py

O desde el shell de Django:
    python manage.py shell
    >>> exec(open('poblar_datos_ejemplo.py').read())
"""

from core.models import Perfil, Skill, Proyecto, Banner
from faq.models import Pregunta
from open.models import Receta
from datetime import date

print("🚀 Iniciando población de datos de ejemplo...")

# 1. Crear Perfil
print("\n📝 Creando perfil...")
perfil, created = Perfil.objects.get_or_create(
    id=1,
    defaults={
        'nombre_completo': 'Tu Nombre Completo',
        'titulo_profesional': 'Desarrollador Web Full Stack',
        'descripcion': 'Soy un desarrollador web apasionado por crear experiencias digitales increíbles. Con experiencia en Django, Python, JavaScript y tecnologías modernas de desarrollo web.',
        'email': 'tu@email.com',
        'telefono': '+57 300 123 4567',
        'linkedin': 'https://linkedin.com/in/tu-perfil',
        'github': 'https://github.com/tu-usuario'
    }
)
print(f"✅ Perfil {'creado' if created else 'ya existe'}")

# 2. Crear Skills
print("\n🎯 Creando skills...")
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
    print(f"  {'✅' if created else '⏭️'} {nombre}")

# 3. Crear Proyectos
print("\n💼 Creando proyectos...")
proyectos_data = [
    {
        'titulo': 'Sistema de Gestión Escolar',
        'descripcion': 'Plataforma web para gestión de estudiantes, profesores y calificaciones. Desarrollada con Django y PostgreSQL.',
        'tecnologias': 'Django, Python, PostgreSQL, Bootstrap',
        'fecha': date(2024, 6, 15),
        'destacado': True,
        'url': 'https://github.com/tu-usuario/proyecto1'
    },
    {
        'titulo': 'E-commerce de Productos Artesanales',
        'descripcion': 'Tienda online con carrito de compras, pasarela de pagos y panel de administración.',
        'tecnologias': 'Django, Stripe, JavaScript, Tailwind CSS',
        'fecha': date(2024, 8, 20),
        'destacado': True,
        'url': 'https://github.com/tu-usuario/proyecto2'
    },
    {
        'titulo': 'Blog Personal con CMS',
        'descripcion': 'Blog con sistema de gestión de contenidos, comentarios y categorías.',
        'tecnologias': 'Django, SQLite, Markdown, Bootstrap',
        'fecha': date(2024, 3, 10),
        'destacado': True,
        'url': 'https://github.com/tu-usuario/proyecto3'
    },
    {
        'titulo': 'API REST para Gestión de Tareas',
        'descripcion': 'API RESTful para aplicación de gestión de tareas con autenticación JWT.',
        'tecnologias': 'Django REST Framework, JWT, PostgreSQL',
        'fecha': date(2024, 5, 5),
        'destacado': False,
        'url': 'https://github.com/tu-usuario/proyecto4'
    },
]

for proyecto_data in proyectos_data:
    proyecto, created = Proyecto.objects.get_or_create(
        titulo=proyecto_data['titulo'],
        defaults=proyecto_data
    )
    print(f"  {'✅' if created else '⏭️'} {proyecto_data['titulo']}")

# 4. Crear Banners con UTM
print("\n🎯 Creando banners con parámetros UTM...")
banners_data = [
    {
        'titulo': 'Portafolio Compañero 1',
        'url': 'https://companero1.railway.app',
        'utm_source': 'mi_home',
        'utm_medium': 'banner',
        'utm_campaign': 'companero1',
        'activo': True,
        'orden': 1
    },
    {
        'titulo': 'Portafolio Compañero 2',
        'url': 'https://companero2.render.com',
        'utm_source': 'mi_home',
        'utm_medium': 'banner',
        'utm_campaign': 'companero2',
        'activo': True,
        'orden': 2
    },
]

for banner_data in banners_data:
    banner, created = Banner.objects.get_or_create(
        titulo=banner_data['titulo'],
        defaults=banner_data
    )
    print(f"  {'✅' if created else '⏭️'} {banner_data['titulo']}")

# 5. Crear Preguntas Frecuentes
print("\n❓ Creando preguntas frecuentes...")
preguntas_data = [
    {
        'titulo': '¿Qué tecnologías utilizas?',
        'respuesta': 'Trabajo principalmente con Python y Django para el backend, JavaScript para el frontend, y bases de datos como PostgreSQL y SQLite. También tengo experiencia con frameworks CSS como Bootstrap y Tailwind.'
    },
    {
        'titulo': '¿Cuánto tiempo llevas programando?',
        'respuesta': 'Llevo aproximadamente 2 años programando profesionalmente, aunque he estado aprendiendo y practicando durante más tiempo. Me especializo en desarrollo web con Django.'
    },
    {
        'titulo': '¿Trabajas de forma remota?',
        'respuesta': 'Sí, tengo experiencia trabajando de forma remota y cuento con todas las herramientas necesarias para colaborar efectivamente en proyectos distribuidos.'
    },
    {
        'titulo': '¿Ofreces servicios de consultoría?',
        'respuesta': 'Sí, ofrezco servicios de consultoría en desarrollo web, arquitectura de aplicaciones Django, y optimización de rendimiento. Contáctame para más detalles.'
    },
    {
        'titulo': '¿Cómo puedo contactarte?',
        'respuesta': 'Puedes contactarme a través del formulario de contacto en este sitio, por email, o a través de mis redes sociales (LinkedIn, GitHub). Respondo generalmente en menos de 24 horas.'
    },
]

for pregunta_data in preguntas_data:
    pregunta, created = Pregunta.objects.get_or_create(
        titulo=pregunta_data['titulo'],
        defaults={'respuesta': pregunta_data['respuesta']}
    )
    print(f"  {'✅' if created else '⏭️'} {pregunta_data['titulo'][:50]}...")

# 6. Crear Recetas
print("\n🍳 Creando recetas...")
recetas_data = [
    {
        'titulo': 'Pasta Carbonara Clásica',
        'resumen': 'Deliciosa pasta italiana con huevo, queso y panceta',
        'descripcion': '''Ingredientes:
- 400g de pasta (espagueti o fettuccine)
- 200g de panceta o tocino
- 4 huevos
- 100g de queso parmesano rallado
- Sal y pimienta negra al gusto

Preparación:
1. Cocina la pasta en agua con sal según las instrucciones del paquete.
2. Mientras tanto, corta la panceta en cubos pequeños y fríela hasta que esté crujiente.
3. En un bowl, bate los huevos con el queso parmesano rallado.
4. Escurre la pasta reservando un poco del agua de cocción.
5. Mezcla la pasta caliente con la panceta y retira del fuego.
6. Agrega la mezcla de huevo y queso, revolviendo rápidamente.
7. Si es necesario, agrega un poco del agua de cocción para crear una salsa cremosa.
8. Sirve inmediatamente con más queso parmesano y pimienta negra.''',
        'palabras_clave': 'pasta, italiana, carbonara, fácil, rápida',
    },
    {
        'titulo': 'Ensalada César',
        'resumen': 'Ensalada fresca con pollo, lechuga romana y aderezo césar',
        'descripcion': '''Ingredientes:
- 2 pechugas de pollo
- 1 lechuga romana grande
- 100g de queso parmesano
- Crutones
- Aderezo césar

Para el aderezo:
- 2 dientes de ajo
- 2 anchoas
- 1 huevo
- Jugo de 1 limón
- 150ml de aceite de oliva
- Sal y pimienta

Preparación:
1. Cocina las pechugas de pollo a la plancha y córtalas en tiras.
2. Lava y corta la lechuga romana en trozos.
3. Prepara el aderezo mezclando todos los ingredientes en una licuadora.
4. En un bowl grande, mezcla la lechuga con el aderezo.
5. Agrega el pollo, crutones y queso parmesano rallado.
6. Sirve inmediatamente.''',
        'palabras_clave': 'ensalada, césar, pollo, saludable, fresca',
    },
    {
        'titulo': 'Tacos al Pastor',
        'resumen': 'Tacos mexicanos con carne marinada y piña',
        'descripcion': '''Ingredientes:
- 500g de carne de cerdo
- 3 chiles guajillo
- 1 cebolla
- Piña fresca
- Tortillas de maíz
- Cilantro y limón

Marinado:
- Achiote
- Jugo de naranja
- Vinagre
- Especias mexicanas

Preparación:
1. Marina la carne con achiote, jugo de naranja y especias por 4 horas.
2. Cocina la carne en una sartén o plancha hasta que esté dorada.
3. Corta la carne en trozos pequeños.
4. Calienta las tortillas.
5. Sirve la carne en las tortillas con cebolla, cilantro, piña y limón.''',
        'palabras_clave': 'mexicana, tacos, pastor, picante, tradicional',
    },
    {
        'titulo': 'Brownie de Chocolate',
        'resumen': 'Postre de chocolate intenso y textura húmeda',
        'descripcion': '''Ingredientes:
- 200g de chocolate negro
- 150g de mantequilla
- 3 huevos
- 200g de azúcar
- 100g de harina
- 1 cucharadita de vainilla

Preparación:
1. Precalienta el horno a 180°C.
2. Derrite el chocolate con la mantequilla a baño maría.
3. Bate los huevos con el azúcar hasta que estén espumosos.
4. Agrega el chocolate derretido y la vainilla.
5. Incorpora la harina tamizada.
6. Vierte en un molde engrasado.
7. Hornea por 25-30 minutos (el centro debe quedar húmedo).
8. Deja enfriar antes de cortar.''',
        'palabras_clave': 'postre, chocolate, brownie, dulce, fácil',
    },
    {
        'titulo': 'Sushi Roll California',
        'resumen': 'Sushi roll con cangrejo, aguacate y pepino',
        'descripcion': '''Ingredientes:
- 2 tazas de arroz para sushi
- Alga nori
- Palitos de cangrejo
- Aguacate
- Pepino
- Mayonesa japonesa
- Semillas de sésamo

Preparación:
1. Cocina el arroz y sazona con vinagre de arroz.
2. Coloca el alga nori sobre una esterilla de bambú.
3. Extiende una capa fina de arroz sobre el alga.
4. Voltea el alga para que el arroz quede abajo.
5. Coloca cangrejo, aguacate y pepino en el centro.
6. Enrolla firmemente usando la esterilla.
7. Corta en 8 piezas iguales.
8. Decora con mayonesa y semillas de sésamo.''',
        'palabras_clave': 'sushi, japonesa, california, roll, saludable',
    },
]

for receta_data in recetas_data:
    receta, created = Receta.objects.get_or_create(
        titulo=receta_data['titulo'],
        defaults=receta_data
    )
    print(f"  {'✅' if created else '⏭️'} {receta_data['titulo']}")

print("\n" + "="*50)
print("✅ ¡Datos de ejemplo creados exitosamente!")
print("="*50)
print("\n📊 Resumen:")
print(f"  - Perfiles: {Perfil.objects.count()}")
print(f"  - Skills: {Skill.objects.count()}")
print(f"  - Proyectos: {Proyecto.objects.count()}")
print(f"  - Banners: {Banner.objects.count()}")
print(f"  - Preguntas: {Pregunta.objects.count()}")
print(f"  - Recetas: {Receta.objects.count()}")
print("\n🌐 Ahora puedes ver tu sitio en: http://127.0.0.1:8000/")
print("🔧 Panel de administración: http://127.0.0.1:8000/admin/")
print("\n⚠️  IMPORTANTE: Estos son datos de ejemplo. Reemplázalos con tu información real.")
