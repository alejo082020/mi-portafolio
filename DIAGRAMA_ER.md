# 📊 Diagrama Entidad-Relación - Base de Datos

## Modelos de la Base de Datos

### 1. **Perfil** (core.Perfil)
Almacena la información personal del portafolio

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Clave primaria |
| nombre_completo | CharField(200) | Nombre completo |
| titulo_profesional | CharField(200) | Título profesional |
| descripcion | TextField | Descripción/biografía |
| foto | ImageField | Foto de perfil |
| email | EmailField | Correo electrónico |
| telefono | CharField(20) | Teléfono (opcional) |
| linkedin | URLField | URL de LinkedIn (opcional) |
| github | URLField | URL de GitHub (opcional) |

**Relaciones:** Ninguna (tabla independiente)

---

### 2. **Skill** (core.Skill)
Habilidades técnicas del portafolio

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Clave primaria |
| nombre | CharField(100) | Nombre de la habilidad |
| nivel | IntegerField | Nivel de dominio (0-100) |
| orden | IntegerField | Orden de visualización |

**Relaciones:** Ninguna (tabla independiente)
**Ordenamiento:** Por campo `orden` (ascendente)

---

### 3. **Proyecto** (core.Proyecto)
Proyectos del portafolio

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Clave primaria |
| titulo | CharField(200) | Título del proyecto |
| descripcion | TextField | Descripción detallada |
| imagen | ImageField | Imagen del proyecto (opcional) |
| url | URLField | URL del proyecto (opcional) |
| tecnologias | CharField(200) | Tecnologías usadas (separadas por comas) |
| fecha | DateField | Fecha del proyecto |
| destacado | BooleanField | Si se muestra en home |

**Relaciones:** Ninguna (tabla independiente)
**Ordenamiento:** Por campo `fecha` (descendente)

---

### 4. **Banner** (core.Banner)
Banners con parámetros UTM para rastreo

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Clave primaria |
| titulo | CharField(200) | Título del banner |
| url | URLField | URL de destino |
| utm_source | CharField(100) | Parámetro UTM source |
| utm_medium | CharField(100) | Parámetro UTM medium |
| utm_campaign | CharField(100) | Parámetro UTM campaign |
| activo | BooleanField | Si está activo |
| orden | IntegerField | Orden de visualización |

**Relaciones:** Ninguna (tabla independiente)
**Ordenamiento:** Por campo `orden` (ascendente)
**Método especial:** `get_url_completa()` - Retorna URL con parámetros UTM

---

### 5. **Contacto** (core.Contacto)
Mensajes de contacto recibidos

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Clave primaria |
| nombre | CharField(100) | Nombre del contacto |
| correo | EmailField | Correo electrónico |
| telefono | CharField(20) | Teléfono (opcional) |
| asunto | CharField(200) | Asunto del mensaje |
| mensaje | TextField | Mensaje completo |
| fecha_envio | DateTimeField | Fecha y hora de envío (auto) |
| leido | BooleanField | Si fue leído por el admin |

**Relaciones:** Ninguna (tabla independiente)
**Ordenamiento:** Por campo `fecha_envio` (descendente)

---

### 6. **Pregunta** (faq.Pregunta)
Preguntas frecuentes

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Clave primaria |
| titulo | CharField(255) | Pregunta |
| respuesta | TextField | Respuesta |

**Relaciones:** Ninguna (tabla independiente)

---

### 7. **Receta** (open.Receta)
Recetas (entidad personalizada para la página open)

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | AutoField | Clave primaria |
| titulo | CharField(200) | Título de la receta |
| resumen | CharField(300) | Resumen breve |
| descripcion | TextField | Descripción completa |
| palabras_clave | CharField(200) | Palabras clave (separadas por comas) |
| imagen | ImageField | Imagen de la receta (opcional) |
| fecha_creacion | DateTimeField | Fecha de creación (auto) |

**Relaciones:** Ninguna (tabla independiente)
**Ordenamiento:** Por campo `fecha_creacion` (descendente)

---

## Diagrama Visual (Texto)

```
┌─────────────────────┐
│      PERFIL         │
├─────────────────────┤
│ id (PK)             │
│ nombre_completo     │
│ titulo_profesional  │
│ descripcion         │
│ foto                │
│ email               │
│ telefono            │
│ linkedin            │
│ github              │
└─────────────────────┘

┌─────────────────────┐
│       SKILL         │
├─────────────────────┤
│ id (PK)             │
│ nombre              │
│ nivel               │
│ orden               │
└─────────────────────┘

┌─────────────────────┐
│     PROYECTO        │
├─────────────────────┤
│ id (PK)             │
│ titulo              │
│ descripcion         │
│ imagen              │
│ url                 │
│ tecnologias         │
│ fecha               │
│ destacado           │
└─────────────────────┘

┌─────────────────────┐
│      BANNER         │
├─────────────────────┤
│ id (PK)             │
│ titulo              │
│ url                 │
│ utm_source          │
│ utm_medium          │
│ utm_campaign        │
│ activo              │
│ orden               │
└─────────────────────┘

┌─────────────────────┐
│     CONTACTO        │
├─────────────────────┤
│ id (PK)             │
│ nombre              │
│ correo              │
│ telefono            │
│ asunto              │
│ mensaje             │
│ fecha_envio         │
│ leido               │
└─────────────────────┘

┌─────────────────────┐
│     PREGUNTA        │
├─────────────────────┤
│ id (PK)             │
│ titulo              │
│ respuesta           │
└─────────────────────┘

┌─────────────────────┐
│      RECETA         │
├─────────────────────┤
│ id (PK)             │
│ titulo              │
│ resumen             │
│ descripcion         │
│ palabras_clave      │
│ imagen              │
│ fecha_creacion      │
└─────────────────────┘
```

## Notas Importantes

1. **No hay relaciones entre tablas**: Todos los modelos son independientes, lo que simplifica la estructura y facilita la gestión desde el CMS.

2. **Campos de imagen**: Los modelos Perfil, Proyecto y Receta tienen campos ImageField que almacenan archivos en la carpeta `media/`.

3. **Campos auto-generados**: 
   - `fecha_envio` en Contacto se genera automáticamente al crear el registro
   - `fecha_creacion` en Receta se genera automáticamente al crear el registro

4. **Ordenamiento predeterminado**:
   - Skill: por `orden` (ascendente)
   - Proyecto: por `fecha` (descendente)
   - Banner: por `orden` (ascendente)
   - Contacto: por `fecha_envio` (descendente)
   - Receta: por `fecha_creacion` (descendente)

5. **Validaciones**:
   - EmailField valida formato de correo electrónico
   - URLField valida formato de URL
   - CharField tiene límites de longitud definidos

## Uso en el CMS (Django Admin)

Todos estos modelos están registrados en el panel de administración de Django (`/admin/`) y pueden ser gestionados completamente desde allí, cumpliendo con el requisito de que **NO se permite hardcode del contenido**.
