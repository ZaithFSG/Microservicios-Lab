# Laboratorio de Microservicios (Django + React)

## Estructura del Proyecto

```text
microservices-lab/
├── docker-compose.yml          # Orquesta los contenedores (postgres, redis, auth, blog)
├── README.md                   # Documentación general del proyecto
│
├── auth-service/               # Servicio de Autenticación (Django)
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   └── users/                  # App de usuarios
│
├── blog-service/              # Servicio de Blog (Django + DRF)
│   └── app/
│       ├── Dockerfile
│       ├── requirements.txt
│       ├── manage.py
│       ├── openapi.yaml       # Documentación de la API
│       ├── blog_service/      # Configuración del proyecto
│       ├── posts/            # App de posts
│       │   └── management/
│       │       └── commands/
│       │           └── seed_blog.py  # Comando para datos de prueba
│       ├── authors/          # App de autores
│       ├── categories/       # App de categorías
│       └── core/            # App central con middlewares
│
├── email-service/            # Servicio de Email (placeholder)
├── frontend/                 # Interfaz de Usuario (placeholder)
└── reverse-proxy/           # Proxy Inverso (placeholder)
```

## Descripción de Componentes

### Blog Service (Puerto 8001)

Microservicio de blog implementado con Django + DRF que incluye:

- Sistema de posts y categorías
- Búsqueda y paginación
- Cache con Redis
- Datos de prueba

### Servicios de Soporte

- PostgreSQL (5432): Base de datos relacional
- Redis (6379): Cache y cola de mensajes

## 🚀 Cómo ejecutar el Blog Service

1. Levantar el servicio:

```bash
docker compose up -d blog
```

2. Verificar que está corriendo:

```bash
docker ps
# Debería mostrar blog_service en puerto 8001
```

3. Probar el healthcheck:

```bash
curl http://localhost:8001/healthz
# Debería devolver {"status": "ok"}
```

## 🌱 Cargar Datos de Prueba

```bash
docker compose exec blog python manage.py seed_blog
```

Esto creará:

- 5 categorías
- 3 autores
- 30 posts (70% publicados, 30% borradores)

## 🧩 Endpoints Disponibles

### Categorías

```bash
# Listar categorías (cacheado por 60s)
GET http://localhost:8001/api/categories/
```

### Posts

```bash
# Listar posts (con paginación)
GET http://localhost:8001/api/posts/?page=1

# Buscar posts
GET http://localhost:8001/api/posts/?search=django

# Detalle de post (cacheado)
GET http://localhost:8001/api/posts/1/
```

## 📦 Verificar Cache Redis

```bash
# Conectar a Redis CLI
docker compose exec redis redis-cli

# Ver claves cacheadas
keys *
```

Deberías ver claves como `:1:views.decorators.cache.cache_page...` después de llamar a los endpoints cacheados.

## 📘 Documentación API

La especificación OpenAPI está disponible en:

```yaml
blog-service/app/openapi.yaml
```