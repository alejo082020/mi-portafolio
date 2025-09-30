# ⚡ Instrucciones Rápidas - Proyecto Portafolio

## 🚀 Inicio Rápido (Primera Vez)

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Aplicar migraciones (ya están hechas)
```bash
python manage.py migrate
```

### 3. Crear superusuario
```bash
python manage.py createsuperuser
```
- Usuario: admin (o el que prefieras)
- Email: tu@email.com
- Contraseña: (elige una segura)

### 4. Ejecutar servidor
```bash
python manage.py runserver
```

### 5. Acceder al sitio
- **Sitio web:** http://127.0.0.1:8000/
- **Panel admin:** http://127.0.0.1:8000/admin/

---

## 📝 Agregar Contenido (IMPORTANTE)

**⚠️ TODO el contenido debe agregarse desde el panel de administración, NO hardcodeado.**

### 1. Agregar tu Perfil
1. Ve a `/admin/` → **Perfil** → **Agregar perfil**
2. Completa:
   - Nombre completo
   - Título profesional
   - Descripción
   - Sube tu foto
   - Email, teléfono
   - URLs de LinkedIn y GitHub
3. Guarda

### 2. Agregar Skills
1. `/admin/` → **Skills** → **Agregar skill**
2. Agrega al menos 5 habilidades:
   - HTML (nivel: 90)
   - CSS (nivel: 85)
   - JavaScript (nivel: 80)
   - Django (nivel: 75)
   - Python (nivel: 85)

### 3. Agregar Proyectos
1. `/admin/` → **Proyectos** → **Agregar proyecto**
2. Agrega al menos 3 proyectos
3. Marca algunos como "destacado" para que aparezcan en home

### 4. Agregar Banners (OBLIGATORIO - Mínimo 2)
1. `/admin/` → **Banners** → **Agregar banner**
2. Banner 1:
   - Título: Portafolio Compañero 1
   - URL: https://sitio-companero1.com
   - UTM Source: mi_home
   - UTM Medium: banner
   - UTM Campaign: companero1
   - Activo: ✓
   - Orden: 1
3. Banner 2:
   - Título: Portafolio Compañero 2
   - URL: https://sitio-companero2.com
   - UTM Source: mi_home
   - UTM Medium: banner
   - UTM Campaign: companero2
   - Activo: ✓
   - Orden: 2

### 5. Agregar Preguntas Frecuentes
1. `/admin/` → **Preguntas** → **Agregar pregunta**
2. Agrega al menos 5 preguntas con sus respuestas

### 6. Agregar Recetas
1. `/admin/` → **Recetas** → **Agregar receta**
2. Agrega al menos 5 recetas con:
   - Título
   - Resumen
   - Descripción
   - Palabras clave (separadas por comas)
   - Imagen (opcional pero recomendado)

---

## 🏷️ Configurar Google Tag Manager

### Paso 1: Obtener ID de GTM
1. Ve a https://tagmanager.google.com/
2. Crea un contenedor
3. Copia tu ID (GTM-XXXXXXX)

### Paso 2: Actualizar el código
1. Abre `templates/base.html`
2. Busca `GTM-XXXX` (2 veces)
3. Reemplaza con tu ID real

### Paso 3: Configurar en GTM
Sigue la guía completa en `GUIA_GTM.md`

---

## 📊 Páginas del Sitio

| URL | Descripción | Requisito |
|-----|-------------|-----------|
| `/` | Home con hoja de vida | ✅ Obligatorio |
| `/contactame/` | Formulario de contacto | ✅ Obligatorio |
| `/faq/` | Preguntas frecuentes | ✅ Obligatorio |
| `/open/` | Lista de recetas (grid) | ✅ Obligatorio |
| `/open/1/` | Detalle de receta | ✅ Obligatorio |
| `/admin/` | Panel de administración | Para gestionar contenido |

---

## ✅ Checklist Antes de Entregar

### Contenido
- [ ] Perfil completo agregado
- [ ] Al menos 5 skills agregadas
- [ ] Al menos 3 proyectos agregados
- [ ] **Mínimo 2 banners con UTM**
- [ ] Al menos 5 preguntas frecuentes
- [ ] Al menos 5 recetas con imágenes

### Funcionalidad
- [ ] Formulario de contacto funciona
- [ ] Validación JavaScript funciona
- [ ] FAQ se expande/colapsa
- [ ] Recetas se muestran en grid
- [ ] Detalle de receta funciona
- [ ] Banners redirigen correctamente

### Google Tag Manager
- [ ] GTM instalado con ID correcto
- [ ] Google Analytics configurado
- [ ] Eventos personalizados configurados
- [ ] Eventos verificados en tiempo real
- [ ] Parámetros UTM verificados

### Despliegue
- [ ] Sitio desplegado online
- [ ] URL funcional
- [ ] Todo funciona en producción

### Documentación
- [ ] README.md completo
- [ ] Capturas de pantalla tomadas
- [ ] Diagrama ER incluido
- [ ] PDF con evidencias preparado

---

## 🐛 Problemas Comunes

### "No module named 'PIL'"
```bash
pip install Pillow
```

### "No such table: core_perfil"
```bash
python manage.py migrate
```

### Las imágenes no se muestran
1. Verifica que `MEDIA_URL` y `MEDIA_ROOT` estén en settings.py
2. Verifica que las URLs incluyan `+ static(settings.MEDIA_URL, ...)`

### El formulario no guarda
1. Verifica que hayas hecho las migraciones
2. Revisa la consola del navegador para errores JavaScript

---

## 📞 Comandos Útiles

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver

# Recolectar archivos estáticos (para producción)
python manage.py collectstatic

# Ver estructura de la BD
python manage.py dbshell

# Limpiar base de datos (CUIDADO)
python manage.py flush
```

---

## 📚 Archivos Importantes

- **`README.md`** - Documentación completa del proyecto
- **`DIAGRAMA_ER.md`** - Diagrama entidad-relación
- **`GUIA_GTM.md`** - Guía completa de Google Tag Manager
- **`GUIA_DESPLIEGUE.md`** - Guía para desplegar online
- **`requirements.txt`** - Dependencias del proyecto
- **`.gitignore`** - Archivos ignorados por Git

---

## 🎯 Criterios de Evaluación

| Criterio | Ponderación | Estado |
|----------|-------------|--------|
| Estructura y contenido en home.html | 5% | ✅ |
| Validación del formulario en contactame.html | 5% | ✅ |
| Contenido dinámico en fyq.html desde CMS | 10% | ✅ |
| Página open.html gestionada desde CMS | 10% | ✅ |
| Implementación de Tag Manager, eventos y UTM | 10% | ⏳ Pendiente configurar |
| Pregunta técnica en sustentación | 10% | ⏳ Prepararse |

**Total implementado:** 40% (falta configurar GTM y desplegar)

---

## 🎓 Temas para Estudiar (Sustentación)

1. **Django:**
   - ¿Qué es un modelo en Django?
   - ¿Cómo funciona el ORM?
   - ¿Qué es una migración?
   - ¿Qué es el admin de Django?

2. **JavaScript:**
   - ¿Cómo funciona la validación del formulario?
   - ¿Qué es el DOM?
   - ¿Qué son los eventos?

3. **Google Analytics:**
   - ¿Qué es Google Tag Manager?
   - ¿Para qué sirven los parámetros UTM?
   - ¿Qué es un evento personalizado?
   - Diferencia entre GTM y GA4

4. **Arquitectura:**
   - Patrón MVC/MTV
   - ¿Qué es un CMS?
   - ¿Por qué no hardcodear contenido?

---

## 🚀 Próximos Pasos

1. **Agregar todo el contenido desde el admin**
2. **Configurar Google Tag Manager** (ver GUIA_GTM.md)
3. **Desplegar el sitio online** (ver GUIA_DESPLIEGUE.md)
4. **Tomar capturas de pantalla**
5. **Preparar documento PDF**
6. **Estudiar para la sustentación**

¡Éxito! 🎉
