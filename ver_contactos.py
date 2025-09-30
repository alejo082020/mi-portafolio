"""
Script para ver todos los contactos en la base de datos
Ejecutar: python ver_contactos.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_portafolio.settings')
django.setup()

from core.models import Contacto

print("\n" + "="*60)
print("📧 MENSAJES DE CONTACTO")
print("="*60 + "\n")

contactos = Contacto.objects.all().order_by('-fecha_envio')

if contactos.exists():
    for i, contacto in enumerate(contactos, 1):
        print(f"Mensaje #{i}")
        print(f"  Nombre: {contacto.nombre}")
        print(f"  Correo: {contacto.correo}")
        print(f"  Teléfono: {contacto.telefono or 'No proporcionado'}")
        print(f"  Asunto: {contacto.asunto}")
        print(f"  Mensaje: {contacto.mensaje[:100]}{'...' if len(contacto.mensaje) > 100 else ''}")
        print(f"  Fecha: {contacto.fecha_envio.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"  Leído: {'Sí' if contacto.leido else 'No'}")
        print("-" * 60)
    
    print(f"\n✅ Total de mensajes: {contactos.count()}")
else:
    print("❌ No hay mensajes de contacto en la base de datos")
    print("\nPosibles causas:")
    print("  1. El formulario no se envió correctamente")
    print("  2. Hay un error en el modelo o la vista")
    print("  3. La base de datos no se actualizó")

print("\n" + "="*60)
