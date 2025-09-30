# 🚀 Guía de Despliegue - Proyecto Portafolio

## Opciones de Despliegue

Este proyecto puede desplegarse en:
1. **Railway** (Recomendado - Fácil y gratis)
2. **Render** (Alternativa gratuita)
3. **PythonAnywhere** (Opción gratuita con limitaciones)

---

## 🚂 Opción 1: Railway (RECOMENDADO)

### Ventajas
- ✅ Despliegue automático desde GitHub
- ✅ Base de datos PostgreSQL incluida
- ✅ SSL/HTTPS automático
- ✅ $5 USD gratis al mes
- ✅ Muy fácil de configurar

### Pasos para desplegar

#### 1. Preparar el proyecto

**Crear archivo `railway.json`:**
```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn mi_portafolio.wsgi",
    "restartPolicyType": "ON_FAILURE",
    "restartPolicyMaxRetries": 10
  }
}
```

**Crear archivo `Procfile`:**
```
web: gunicorn mi_portafolio.wsgi
```

**Actualizar `requirements.txt`:**
```
Django>=4.2,<5.0
Pillow>=10.0.0
whitenoise>=6.5.0
gunicorn>=21.2.0
psycopg2-binary>=2.9.9
```

**Actualizar `settings.py`:**

Agrega al final del archivo:

```python
import os
import dj_database_url

# Configuración para producción
if 'RAILWAY_ENVIRONMENT' in os.environ:
    DEBUG = False
    ALLOWED_HOSTS = ['.railway.app', 'tu-dominio.com']
    
    # Base de datos PostgreSQL
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
    
    # Seguridad
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
```

#### 2. Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tu-usuario/tu-repo.git
git push -u origin main
```

#### 3. Desplegar en Railway

1. Ve a https://railway.app/
2. Haz clic en "Start a New Project"
3. Selecciona "Deploy from GitHub repo"
4. Conecta tu cuenta de GitHub
5. Selecciona tu repositorio
6. Railway detectará automáticamente Django
7. Agrega una base de datos PostgreSQL:
   - Haz clic en "+ New"
   - Selecciona "Database" → "PostgreSQL"
8. Railway generará automáticamente la variable `DATABASE_URL`

#### 4. Configurar variables de entorno

En Railway, ve a tu proyecto → Variables:

```
SECRET_KEY=tu-secret-key-super-segura-aqui
RAILWAY_ENVIRONMENT=production
```

Para generar un SECRET_KEY seguro:
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

#### 5. Crear superusuario

Una vez desplegado:
1. Ve a tu proyecto en Railway
2. Haz clic en tu servicio web
3. Ve a la pestaña "Settings"
4. Busca "Service Domain" y copia la URL
5. En tu terminal local:

```bash
# Instalar Railway CLI
npm i -g @railway/cli

# Login
railway login

# Conectar al proyecto
railway link

# Ejecutar comando en Railway
railway run python manage.py createsuperuser
```

O usa la terminal web de Railway directamente.

---

## 🎨 Opción 2: Render

### Pasos para desplegar

#### 1. Preparar el proyecto

**Crear archivo `build.sh`:**
```bash
#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
```

Dale permisos de ejecución:
```bash
chmod +x build.sh
```

**Actualizar `requirements.txt`:**
```
Django>=4.2,<5.0
Pillow>=10.0.0
whitenoise>=6.5.0
gunicorn>=21.2.0
psycopg2-binary>=2.9.9
dj-database-url>=2.1.0
```

**Actualizar `settings.py`:**
```python
import os
import dj_database_url

# Configuración para producción
if 'RENDER' in os.environ:
    DEBUG = False
    ALLOWED_HOSTS = ['.onrender.com']
    
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
```

#### 2. Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git push
```

#### 3. Desplegar en Render

1. Ve a https://render.com/
2. Crea una cuenta
3. Haz clic en "New +" → "Web Service"
4. Conecta tu repositorio de GitHub
5. Configura:
   - **Name:** mi-portafolio
   - **Environment:** Python 3
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn mi_portafolio.wsgi:application`
6. Agrega variables de entorno:
   - `SECRET_KEY`: tu-secret-key
   - `PYTHON_VERSION`: 3.11.0
7. Crea una base de datos PostgreSQL:
   - "New +" → "PostgreSQL"
   - Copia la "Internal Database URL"
   - Agrégala como variable `DATABASE_URL` en tu web service

---

## 🐍 Opción 3: PythonAnywhere

### Pasos para desplegar

1. Crea cuenta en https://www.pythonanywhere.com/
2. Ve a "Web" → "Add a new web app"
3. Selecciona "Manual configuration" → Python 3.10
4. En "Code", configura:
   - Source code: `/home/tuusuario/proyecto_portafolio`
   - Working directory: `/home/tuusuario/proyecto_portafolio`
5. En "Virtualenv", crea uno nuevo:
   ```
   /home/tuusuario/.virtualenvs/portafolio
   ```
6. Abre una consola Bash y ejecuta:
   ```bash
   cd ~
   git clone https://github.com/tu-usuario/tu-repo.git proyecto_portafolio
   cd proyecto_portafolio
   mkvirtualenv --python=/usr/bin/python3.10 portafolio
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic
   python manage.py createsuperuser
   ```
7. Configura el WSGI file (en la pestaña Web):
   ```python
   import os
   import sys
   
   path = '/home/tuusuario/proyecto_portafolio'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'mi_portafolio.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```
8. Recarga la aplicación web

---

## ✅ Verificación Post-Despliegue

### 1. Verificar que el sitio carga
- [ ] La página principal se ve correctamente
- [ ] Los estilos CSS se cargan
- [ ] Las imágenes se muestran

### 2. Verificar funcionalidades
- [ ] Navegación entre páginas funciona
- [ ] Formulario de contacto funciona
- [ ] FAQ se expande/colapsa
- [ ] Recetas se muestran correctamente
- [ ] Links de banners funcionan

### 3. Verificar admin
- [ ] Puedes acceder a `/admin/`
- [ ] Puedes agregar/editar contenido
- [ ] Las imágenes se suben correctamente

### 4. Verificar GTM y Analytics
- [ ] GTM se carga (verifica en DevTools)
- [ ] Eventos se disparan
- [ ] Aparecen en Google Analytics tiempo real

---

## 🐛 Solución de Problemas Comunes

### Error: "DisallowedHost"
**Solución:** Agrega tu dominio a `ALLOWED_HOSTS` en `settings.py`

### Error: "Static files not found"
**Solución:** Ejecuta `python manage.py collectstatic`

### Error: "Database connection failed"
**Solución:** Verifica que la variable `DATABASE_URL` esté configurada

### Las imágenes no se cargan
**Solución:** 
- Verifica que `MEDIA_URL` y `MEDIA_ROOT` estén configurados
- En producción, considera usar un servicio como Cloudinary o AWS S3

### Error 500 en producción
**Solución:**
1. Activa temporalmente `DEBUG = True` para ver el error
2. Revisa los logs en tu plataforma de hosting
3. Verifica que todas las migraciones se aplicaron

---

## 📝 Checklist de Entrega

- [ ] Sitio desplegado y funcionando online
- [ ] URL del sitio agregada al README
- [ ] Repositorio de GitHub público
- [ ] README con instrucciones claras
- [ ] Documento PDF con:
  - [ ] Diagrama entidad-relación
  - [ ] Capturas del sitio funcionando
  - [ ] Capturas de Google Analytics
  - [ ] Capturas de eventos marcados
  - [ ] Capturas de parámetros UTM
- [ ] Contenido agregado desde el CMS (no hardcoded)
- [ ] Al menos 2 banners con UTM funcionando
- [ ] Formulario de contacto validado
- [ ] FAQ con accordion funcional
- [ ] Página open con grid de recetas

---

## 🎓 Para la Sustentación

Prepárate para:
1. Mostrar el sitio funcionando online
2. Explicar la arquitectura del proyecto
3. Mostrar el código de validación JavaScript
4. Explicar cómo funciona el CMS
5. Demostrar eventos en Google Analytics
6. Mostrar parámetros UTM en Analytics
7. Responder pregunta técnica del profesor

¡Éxito en tu proyecto! 🚀
