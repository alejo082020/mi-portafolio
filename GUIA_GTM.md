# 📊 Guía de Configuración - Google Tag Manager y Analytics

## 🎯 Paso 1: Crear Cuenta en Google Tag Manager

1. Ve a https://tagmanager.google.com/
2. Haz clic en "Crear cuenta"
3. Completa los datos:
   - **Nombre de la cuenta:** Tu nombre o empresa
   - **País:** Colombia (o tu país)
   - **Nombre del contenedor:** Nombre de tu sitio
   - **Plataforma de destino:** Web
4. Acepta los términos de servicio
5. **Copia el ID del contenedor** (formato: GTM-XXXXXXX)

## 🔧 Paso 2: Instalar GTM en tu Sitio

El código ya está instalado en `templates/base.html`, solo necesitas:

1. Abrir `templates/base.html`
2. Buscar `GTM-XXXX` (aparece 2 veces)
3. Reemplazar con tu ID real (ej: `GTM-ABC1234`)

**Ubicaciones del código:**
- Línea 14: Script en el `<head>`
- Línea 63: Noscript después del `<body>`

## 📈 Paso 3: Crear Propiedad en Google Analytics 4

1. Ve a https://analytics.google.com/
2. Haz clic en "Administrador" (engranaje abajo a la izquierda)
3. Crea una propiedad:
   - **Nombre de la propiedad:** Portafolio [Tu Nombre]
   - **Zona horaria:** (GMT-05:00) Bogotá
   - **Moneda:** Peso colombiano (COP)
4. Completa los detalles del negocio
5. **Copia el ID de medición** (formato: G-XXXXXXXXXX)

## 🏷️ Paso 4: Configurar Etiqueta de Google Analytics en GTM

### 4.1 Crear la etiqueta principal

1. En GTM, ve a **Etiquetas** → **Nueva**
2. Configuración de la etiqueta:
   - **Tipo:** Google Analytics: Etiqueta de Google
   - **ID de medición:** Pega tu G-XXXXXXXXXX
3. Activación:
   - **Activador:** All Pages (Todas las páginas)
4. Nombra la etiqueta: "GA4 - Configuración"
5. Guarda

### 4.2 Verificar instalación

1. En GTM, haz clic en **Vista previa**
2. Ingresa la URL de tu sitio local: `http://127.0.0.1:8000`
3. Navega por tu sitio
4. Verifica que la etiqueta GA4 se dispare en todas las páginas

## 🎯 Paso 5: Configurar Eventos Personalizados

Tu sitio ya tiene estos eventos marcados en el código. Ahora debes configurarlos en GTM:

### Evento 1: Clic en Banner (banner_click)

**Crear Variable:**
1. Variables → Nueva → Variable de capa de datos
2. Nombre: `banner_name`
3. Nombre de la variable de capa de datos: `banner_name`

**Crear Activador:**
1. Activadores → Nuevo
2. Tipo: Evento personalizado
3. Nombre del evento: `banner_click`
4. Nombre: "Evento - Clic en Banner"

**Crear Etiqueta:**
1. Etiquetas → Nueva
2. Tipo: Evento de Google Analytics: GA4
3. ID de medición: Tu G-XXXXXXXXXX
4. Nombre del evento: `banner_click`
5. Parámetros del evento:
   - Nombre: `banner_name`
   - Valor: `{{banner_name}}`
6. Activador: "Evento - Clic en Banner"
7. Nombre: "GA4 - Banner Click"

### Evento 2: Envío de Formulario (form_submit)

**Crear Activador:**
1. Activadores → Nuevo
2. Tipo: Evento personalizado
3. Nombre del evento: `form_submit`
4. Nombre: "Evento - Form Submit"

**Crear Etiqueta:**
1. Etiquetas → Nueva
2. Tipo: Evento de Google Analytics: GA4
3. ID de medición: Tu G-XXXXXXXXXX
4. Nombre del evento: `form_submit`
5. Parámetros del evento:
   - Nombre: `form_name`
   - Valor: `contacto`
6. Activador: "Evento - Form Submit"
7. Nombre: "GA4 - Form Submit"

### Evento 3: Formulario Exitoso (form_success)

**Crear Activador:**
1. Activadores → Nuevo
2. Tipo: Evento personalizado
3. Nombre del evento: `form_success`
4. Nombre: "Evento - Form Success"

**Crear Etiqueta:**
1. Etiquetas → Nueva
2. Tipo: Evento de Google Analytics: GA4
3. ID de medición: Tu G-XXXXXXXXXX
4. Nombre del evento: `form_success`
5. Activador: "Evento - Form Success"
6. Nombre: "GA4 - Form Success"

### Evento 4: Clic en FAQ (faq_click)

**Crear Activador:**
1. Activadores → Nuevo
2. Tipo: Evento personalizado
3. Nombre del evento: `faq_click`
4. Nombre: "Evento - FAQ Click"

**Crear Etiqueta:**
1. Etiquetas → Nueva
2. Tipo: Evento de Google Analytics: GA4
3. ID de medición: Tu G-XXXXXXXXXX
4. Nombre del evento: `faq_click`
5. Activador: "Evento - FAQ Click"
6. Nombre: "GA4 - FAQ Click"

### Evento 5: Ver Receta (recipe_view)

**Crear Activador:**
1. Activadores → Nuevo
2. Tipo: Evento personalizado
3. Nombre del evento: `recipe_view`
4. Nombre: "Evento - Recipe View"

**Crear Etiqueta:**
1. Etiquetas → Nueva
2. Tipo: Evento de Google Analytics: GA4
3. ID de medición: Tu G-XXXXXXXXXX
4. Nombre del evento: `recipe_view`
5. Activador: "Evento - Recipe View"
6. Nombre: "GA4 - Recipe View"

### Evento 6: Detalle de Receta (recipe_detail_view)

**Crear Activador:**
1. Activadores → Nuevo
2. Tipo: Evento personalizado
3. Nombre del evento: `recipe_detail_view`
4. Nombre: "Evento - Recipe Detail View"

**Crear Etiqueta:**
1. Etiquetas → Nueva
2. Tipo: Evento de Google Analytics: GA4
3. ID de medición: Tu G-XXXXXXXXXX
4. Nombre del evento: `recipe_detail_view`
5. Activador: "Evento - Recipe Detail View"
6. Nombre: "GA4 - Recipe Detail View"

## 📊 Paso 6: Publicar Contenedor

1. En GTM, haz clic en **Enviar** (arriba a la derecha)
2. Nombre de la versión: "Configuración inicial"
3. Descripción: "GA4 + Eventos personalizados"
4. Haz clic en **Publicar**

## ✅ Paso 7: Verificar Eventos en Google Analytics

### Método 1: Tiempo Real

1. Ve a Google Analytics
2. Menú izquierdo → **Informes** → **Tiempo real**
3. Abre tu sitio en otra pestaña
4. Realiza acciones (clic en banners, enviar formulario, etc.)
5. Verifica que los eventos aparezcan en tiempo real

### Método 2: DebugView

1. En Google Analytics, ve a **Configurar** → **DebugView**
2. En GTM, activa el modo de vista previa
3. Navega por tu sitio
4. Verifica los eventos en DebugView

## 🔍 Paso 8: Verificar Parámetros UTM

Los banners ya tienen parámetros UTM configurados. Para verificarlos:

1. En Google Analytics, ve a **Informes** → **Adquisición** → **Adquisición de tráfico**
2. Filtra por:
   - **Fuente/medio:** Verás `mi_home / banner`
   - **Campaña:** Verás los nombres de las campañas de tus banners

### Crear Banners con UTM en el Admin

1. Ve a `/admin/` → **Banners** → **Agregar banner**
2. Completa:
   - **Título:** Compañero 1
   - **URL:** https://sitio-companero1.com
   - **UTM Source:** mi_home
   - **UTM Medium:** banner
   - **UTM Campaign:** companero1
   - **Activo:** ✓
   - **Orden:** 1
3. Guarda

Repite para al menos 2 banners (requisito del proyecto).

## 📸 Capturas Requeridas para la Entrega

Debes tomar capturas de pantalla de:

1. **Google Tag Manager:**
   - Lista de etiquetas configuradas
   - Vista previa mostrando eventos disparándose

2. **Google Analytics:**
   - Informe de tiempo real mostrando eventos
   - Informe de adquisición mostrando parámetros UTM
   - DebugView mostrando eventos personalizados

3. **Sitio funcionando:**
   - Home con banners
   - Formulario de contacto
   - FAQ funcionando
   - Página de recetas

## 🐛 Solución de Problemas

### Los eventos no aparecen en Analytics

1. Verifica que el ID de medición sea correcto
2. Revisa la consola del navegador (F12) para errores
3. Usa el modo de vista previa de GTM
4. Espera 24-48 horas para datos históricos (tiempo real es inmediato)

### Los parámetros UTM no se ven

1. Verifica que los banners estén marcados como "activos"
2. Asegúrate de hacer clic en los banners desde tu sitio
3. Los parámetros UTM solo funcionan en el sitio publicado online

### GTM no se carga

1. Verifica que reemplazaste GTM-XXXX con tu ID real
2. Revisa que el código esté en ambas ubicaciones (head y body)
3. Limpia caché del navegador

## 📝 Checklist Final

- [ ] GTM instalado con ID correcto
- [ ] Propiedad GA4 creada
- [ ] Etiqueta GA4 configurada en GTM
- [ ] 6 eventos personalizados configurados
- [ ] Contenedor GTM publicado
- [ ] Eventos verificados en tiempo real
- [ ] Al menos 2 banners con UTM creados
- [ ] Parámetros UTM verificados en Analytics
- [ ] Capturas de pantalla tomadas

## 🎓 Para la Sustentación

Prepárate para explicar:
- Qué es Google Tag Manager y por qué se usa
- Diferencia entre GTM y Google Analytics
- Qué son los parámetros UTM y para qué sirven
- Cómo funcionan los eventos personalizados
- Cómo verificaste que todo funciona correctamente
