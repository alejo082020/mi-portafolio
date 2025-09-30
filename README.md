# 🎓 Proyecto Final - Ingeniería Web

## 📋 Descripción del Proyecto

Este es un sitio web de portafolio personal desarrollado con Django como CMS, que incluye:
- Página de inicio con hoja de vida
- Sistema de gestión de contenidos dinámico
- Formulario de contacto con validación JavaScript
- Sección de preguntas frecuentes (FAQ)
- Galería de recetas gestionada desde el CMS
- Integración con Google Tag Manager y Google Analytics
- Seguimiento de eventos y parámetros UTM

## 🚀 Tecnologías Utilizadas

- **Backend:** Django 4.x
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Estilos:** Bootstrap 5.3
- **Base de datos:** SQLite (desarrollo)
- **Analítica:** Google Tag Manager, Google Analytics 4
- **Despliegue:** Compatible con Vercel, Railway, Netlify

## 📁 Estructura del Proyecto

```
proyecto_portafolio/
├── core/                   # App principal (home, contacto, perfil)
│   ├── models.py          # Modelos: Perfil, Skill, Proyecto, Banner, Contacto
│   ├── views.py           # Vistas principales
│   ├── forms.py           # Formulario de contacto
│   └── admin.py           # Configuración del admin
├── faq/                    # App de preguntas frecuentes
│   ├── models.py          # Modelo: Pregunta
│   └── views.py           # Vista de FAQ
├── open/                   # App de recetas (entidad personalizada)
│   ├── models.py          # Modelo: Receta
│   └── views.py           # Vistas de recetas
├── templates/              # Templates HTML
│   ├── base.html          # Template base
│   ├── home.html          # Página principal
│   ├── contactame.html    # Formulario de contacto
│   ├── fyq.html           # Preguntas frecuentes
│   ├── open.html          # Lista de recetas
│   └── open_detail.html   # Detalle de receta
├── static/                 # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
├── media/                  # Archivos subidos por usuarios
└── manage.py              # Script de gestión de Django
```

## 🔧 Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <tu-repositorio>
cd proyecto_portafolio
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install django pillow whitenoise
```

### 5. Crear archivo requirements.txt

```bash
pip freeze > requirements.txt
```

### 6. Realizar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Crear superusuario

```bash
python manage.py createsuperuser
```

### 8. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

El sitio estará disponible en: `http://127.0.0.1:8000/`

## 📊 Configuración de Google Tag Manager

### 1. Crear cuenta en Google Tag Manager
- Ve a https://tagmanager.google.com/
- Crea un contenedor para tu sitio web
- Copia el ID del contenedor (GTM-XXXX)

### 2. Reemplazar el ID en base.html
- Abre `templates/base.html`
- Busca `GTM-XXXX` (aparece 2 veces)
- Reemplázalo con tu ID real

### 3. Configurar Google Analytics 4
- Crea una propiedad en Google Analytics
- En GTM, agrega una etiqueta de Google Analytics
- Configura los eventos personalizados:
  - `banner_click`: Clic en banners con UTM
  - `form_submit`: Envío de formulario
  - `form_success`: Formulario enviado exitosamente
  - `faq_click`: Clic en preguntas frecuentes
  - `recipe_view`: Visualización de receta
  - `recipe_detail_view`: Vista detallada de receta

## 🎯 Funcionalidades Implementadas

### ✅ Página home.html (index)
- [x] Hoja de vida con foto de perfil
- [x] Perfil profesional
- [x] Portafolio de proyectos
- [x] Lista de skills
- [x] Datos de contacto
- [x] Mínimo 2 banners con parámetros UTM
- [x] Todo el contenido gestionable desde el CMS

### ✅ Página contactame.html
- [x] Formulario web funcional
- [x] Validación de campos con JavaScript
- [x] Validación del lado del servidor (Django)
- [x] Protección CSRF
- [x] Almacenamiento en base de datos
- [x] Página de confirmación

### ✅ Página fyq.html
- [x] Preguntas frecuentes desde CMS
- [x] Interfaz expandible/colapsable (accordion)
- [x] Diseño profesional UX/UI
- [x] Eventos marcados en GTM

### ✅ Página open.html
- [x] Vista en formato grid
- [x] Entidad personalizada (Recetas)
- [x] Campos: imagen, título, resumen, descripción, palabras clave
- [x] Link a ver detalle
- [x] Gestionable desde CMS

### ✅ Integración de Analítica
- [x] Google Tag Manager integrado
- [x] Google Analytics 4 configurado
- [x] Eventos personalizados marcados
- [x] Parámetros UTM en banners

## 📝 Uso del Panel de Administración

### Acceder al admin
1. Ve a `http://127.0.0.1:8000/admin/`
2. Ingresa con tu superusuario

### Gestionar contenido

**Perfil:**
- Agrega tu información personal
- Sube tu foto de perfil
- Configura enlaces a redes sociales

**Skills:**
- Agrega tus habilidades técnicas
- Define el nivel de cada skill
- Ordena según prioridad

**Proyectos:**
- Agrega tus proyectos destacados
- Sube imágenes
- Marca como destacados para mostrar en home

**Banners:**
- Crea banners con URLs de compañeros
- Configura parámetros UTM (source, medium, campaign)
- Activa/desactiva banners
- Define el orden de aparición

**Preguntas Frecuentes:**
- Agrega preguntas y respuestas
- Edita contenido dinámicamente

**Recetas:**
- Agrega recetas con imagen
- Define título, resumen, descripción
- Agrega palabras clave separadas por comas

**Contactos:**
- Revisa mensajes recibidos
- Marca como leídos

## 🚀 Despliegue en Producción

### Preparar para producción

1. **Actualizar settings.py:**
```python
DEBUG = False
ALLOWED_HOSTS = ['tu-dominio.com', 'www.tu-dominio.com']
```

2. **Recolectar archivos estáticos:**
```bash
python manage.py collectstatic
```

3. **Configurar variables de entorno:**
- SECRET_KEY
- DATABASE_URL (si usas PostgreSQL)
- ALLOWED_HOSTS

### Desplegar en Railway

1. Crea cuenta en Railway.app
2. Conecta tu repositorio de GitHub
3. Railway detectará automáticamente Django
4. Configura las variables de entorno
5. Despliega

### Desplegar en Vercel

1. Instala vercel CLI: `npm i -g vercel`
2. Crea archivo `vercel.json` en la raíz
3. Ejecuta: `vercel`
4. Sigue las instrucciones

## 📸 Capturas de Pantalla

Incluye en tu entrega:
- Captura del sitio en funcionamiento
- Captura de Google Analytics mostrando eventos
- Captura de parámetros UTM en Analytics
- Diagrama entidad-relación de la base de datos

## 🎓 Criterios de Evaluación Cumplidos

- ✅ Estructura y contenido en home.html (5%)
- ✅ Validación del formulario en contactame.html (5%)
- ✅ Contenido dinámico en fyq.html desde CMS (10%)
- ✅ Página open.html gestionada desde CMS (10%)
- ✅ Implementación de Tag Manager, eventos y UTM (10%)
- ✅ Publicación online (pendiente de desplegar)
- ✅ Pregunta técnica en sustentación (preparado)

## 📚 Recursos Adicionales

- [Documentación de Django](https://docs.djangoproject.com/)
- [Bootstrap 5 Docs](https://getbootstrap.com/docs/5.3/)
- [Google Tag Manager](https://tagmanager.google.com/)
- [Google Analytics 4](https://analytics.google.com/)

## 👨‍💻 Autor

Tu Nombre - Ingeniería Web

## 📄 Licencia

Este proyecto es para fines educativos.
