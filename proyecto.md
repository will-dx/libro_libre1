# ESPECIFICACIONES DEL PROYECTO LIBROLIBRE

## Descripción General

LibroLibre es una aplicación web orientada a estudiantes universitarios que permite publicar, prestar o donar libros académicos entre alumnos de una misma institución.

El sistema debe facilitar la búsqueda de libros, la comunicación entre estudiantes y la coordinación de puntos de encuentro para realizar entregas de forma organizada.

---

# Stack Tecnológico

El proyecto debe desarrollarse utilizando exclusivamente:

## Backend

* Python
* Django

## Frontend

* HTML5
* CSS3

## Base de Datos

* PostgreSQL

## Hosting

* Render

## Control de Versiones

* GitHub

## Sistema de Mapas

* Leaflet
* OpenStreetMap

## Procesamiento de Imágenes

* Pillow

No utilizar:

* SQLite
* React
* Vue
* Angular

---

# Arquitectura General

El sistema estará dividido en los siguientes módulos:

* Usuarios
* Libros
* Solicitudes
* Mensajería
* Puntos de Encuentro
* Administración

Todas las relaciones entre modelos deben definirse antes de crear vistas o formularios.

---

# Configuración de Base de Datos

## Requisito Obligatorio

El proyecto debe utilizar PostgreSQL de Render desde el inicio del desarrollo.

No debe utilizarse SQLite en ninguna etapa.

## Objetivo

Evitar problemas de:

* Migraciones incompatibles
* Tablas inexistentes
* Datos perdidos
* Relaciones rotas
* Errores al desplegar

## Flujo Correcto

1. Crear PostgreSQL en Render.
2. Obtener DATABASE_URL.
3. Configurar Django para PostgreSQL.
4. Crear modelos.
5. Crear migraciones.
6. Ejecutar migraciones.
7. Desarrollar funcionalidades.
8. Desplegar en Render.

---

# Sistema de Usuarios

## Registro

El formulario de registro debe contener:

* Nombre completo
* Nombre de usuario
* Correo institucional
* Contraseña
* Confirmar contraseña

## Validaciones

* Todos los campos son obligatorios.
* El correo debe ser único.
* El nombre de usuario debe ser único.
* La contraseña debe tener una longitud mínima definida.
* Confirmar contraseña debe coincidir exactamente con la contraseña.
* Mostrar mensajes claros cuando exista un error.

---

# Inicio de Sesión

Los usuarios podrán iniciar sesión utilizando:

* Nombre de usuario
* Contraseña

Debe utilizarse el sistema de autenticación de Django.

---

# Recuperación de Contraseña

El sistema debe permitir recuperar la contraseña mediante correo electrónico.

---

# Gestión de Libros

Los usuarios autenticados podrán publicar libros.

## Campos

* Título
* Autor
* Descripción
* Tipo de publicación
* Imagen de portada
* Estado de disponibilidad
* Fecha de publicación

## Tipos de Publicación

* Préstamo
* Donación

## Disponibilidad

* Disponible
* No disponible

---

# Gestión de Imágenes

La imagen de portada es obligatoria.

## Formatos Permitidos

* JPG
* JPEG
* PNG
* WEBP

## Requisitos

* Guardar correctamente la imagen.
* Asociar la imagen al libro correspondiente.
* Mostrar la imagen en el catálogo.
* Mostrar la imagen en el detalle del libro.
* Mostrar la imagen en el perfil del propietario.

## Casos de Error

Si la imagen no se carga:

* No crear el libro.
* Mostrar mensaje de error.
* No guardar registros incompletos.

## Compatibilidad con Render

Las rutas de imágenes deben ser compatibles con despliegue.

No utilizar rutas locales absolutas.

---

# Catálogo de Libros

La página principal mostrará:

* Imagen de portada
* Título
* Autor
* Tipo de publicación
* Disponibilidad
* Botón de solicitud

Debe existir:

* Barra de búsqueda
* Filtro por autor
* Filtro por disponibilidad
* Filtro por tipo de publicación

---

# Detalle de Libro

La vista detallada debe mostrar:

* Portada
* Título
* Autor
* Descripción
* Tipo de publicación
* Estado
* Información del propietario

---

# Sistema de Solicitudes

Cuando un usuario solicite un libro:

1. Se crea una solicitud.
2. El propietario recibe una notificación.
3. Puede aceptar o rechazar.

## Estados

* Pendiente
* Aceptada
* Rechazada
* Cancelada
* Completada

---

# Sistema de Mensajería

Cuando una solicitud sea aceptada:

* Se habilita un chat privado.
* Solo participan propietario y solicitante.
* Los mensajes quedan asociados a la solicitud.

## Funciones

* Enviar mensajes.
* Ver historial.
* Coordinar entrega.

---

# Sistema de Mapas

## Objetivo

Permitir coordinar la entrega del libro.

## Funcionamiento

Cuando una solicitud sea aceptada:

1. El propietario abre el mapa.
2. Selecciona un punto de encuentro.
3. Se guardan las coordenadas.
4. El solicitante visualiza la ubicación.

## Información a Guardar

* Latitud
* Longitud
* Dirección
* Fecha de entrega
* Hora de entrega

## Restricciones

* Solo un punto activo por solicitud.
* Solo usuarios involucrados pueden acceder.

---

# Perfil del Usuario

Cada usuario tendrá acceso a:

## Mis Libros

* Disponibles
* Prestados
* Donados

## Solicitudes Recibidas

* Pendientes
* Aceptadas
* Rechazadas

## Solicitudes Realizadas

* Historial completo

---

# Panel Administrativo

El administrador podrá:

* Gestionar usuarios.
* Gestionar libros.
* Gestionar solicitudes.
* Gestionar mensajes.
* Gestionar puntos de encuentro.
* Eliminar contenido inapropiado.

---

# Entidades Principales

## Usuario

Información de estudiantes registrados.

## Libro

Información de libros publicados.

## Solicitud

Registro de solicitudes realizadas.

## Mensaje

Conversaciones privadas.

## PuntoEncuentro

Ubicaciones de entrega.

---

# Requisitos de Seguridad

* Todas las vistas privadas requieren autenticación.
* Los usuarios solo pueden modificar sus propios libros.
* Los usuarios solo pueden ver sus propias solicitudes.
* El chat debe estar protegido.
* El punto de encuentro solo debe ser visible para los participantes.

---

# Variables de Entorno

Configurar:

* SECRET_KEY
* DEBUG
* DATABASE_URL
* ALLOWED_HOSTS

---

# Archivos Estáticos y Multimedia

Configurar correctamente:

* STATIC_URL
* STATIC_ROOT
* MEDIA_URL
* MEDIA_ROOT

Las imágenes deben visualizarse correctamente después del despliegue.

---

# Pruebas Obligatorias

Antes de cada despliegue verificar:

* Registro de usuarios.
* Inicio de sesión.
* Recuperación de contraseña.
* Publicación de libros.
* Carga de imágenes.
* Visualización de imágenes.
* Solicitudes.
* Mensajería.
* Mapa.
* Punto de encuentro.
* Conexión PostgreSQL.
* Migraciones aplicadas.

---

# Objetivo Final

Construir una plataforma web universitaria que permita publicar, solicitar, prestar o donar libros académicos, incorporando autenticación segura, gestión de imágenes, mensajería privada y coordinación de entregas mediante mapas interactivos, utilizando Django, Python, HTML, CSS, PostgreSQL y Render como entorno único de desarrollo y producción.
