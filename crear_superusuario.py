"""
Script para crear superusuario automáticamente en Railway
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_portafolio.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Crear superusuario solo si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        username='admin',
        email='admin@portafolio.com',
        password='admin123'  # CAMBIAR ESTO después del primer login
    )
    print("✅ Superusuario 'admin' creado exitosamente")
    print("   Usuario: admin")
    print("   Password: admin123")
    print("   ⚠️  IMPORTANTE: Cambia la contraseña después del primer login")
else:
    print("⏭️  Superusuario ya existe")
