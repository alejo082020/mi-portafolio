"""
Script para agregar banners con parámetros UTM
Ejecutar: python manage.py shell < agregar_banners.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_portafolio.settings')
django.setup()

from core.models import Banner

print("🎯 Agregando banners con parámetros UTM...")

# Banner 1
banner1, created1 = Banner.objects.get_or_create(
    titulo='NICOLAS PARRA',
    defaults={
        'url': 'https://cv-nicolas-torres.up.railway.app?utm_source=friend&utm_medium=referral&utm_campaign=friend_referral&utm_id=Friend+Referral ',
        'utm_source': 'mi_home',
        'utm_medium': 'banner',
        'utm_campaign': 'companero1',
        'activo': True,
        'orden': 1
    }
)
print(f"  {'✅ Creado' if created1 else '⏭️  Ya existe'}: {banner1.titulo}")

# Banner 2
banner2, created2 = Banner.objects.get_or_create(
    titulo='Portafolio Compañero 2',
    defaults={
        'url': 'https://companero2-portafolio.render.com',
        'utm_source': 'mi_home',
        'utm_medium': 'banner',
        'utm_campaign': 'companero2',
        'activo': True,
        'orden': 2
    }
)
print(f"  {'✅ Creado' if created2 else '⏭️  Ya existe'}: {banner2.titulo}")

# Banner 3 (extra)
banner3, created3 = Banner.objects.get_or_create(
    titulo='Proyecto Destacado',
    defaults={
        'url': 'https://github.com/tu-usuario/proyecto-destacado',
        'utm_source': 'mi_home',
        'utm_medium': 'banner',
        'utm_campaign': 'proyecto_destacado',
        'activo': True,
        'orden': 3
    }
)
print(f"  {'✅ Creado' if created3 else '⏭️  Ya existe'}: {banner3.titulo}")

print("\n✅ ¡Banners agregados exitosamente!")
print(f"\nTotal de banners activos: {Banner.objects.filter(activo=True).count()}")
print("\n🌐 Recarga tu página para verlos: http://127.0.0.1:8080/")
print("\n📊 URLs completas con UTM:")
for banner in Banner.objects.filter(activo=True).order_by('orden'):
    print(f"  - {banner.titulo}: {banner.get_url_completa()}")
