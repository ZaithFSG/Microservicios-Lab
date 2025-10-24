# Laboratorio de Microservicios (Django + React)

## Estructura del Proyecto

```text
microservices-lab/
├── docker-compose.yml          # Orquesta los contenedores (postgres, redis, auth, ...)
├── README_GENERAL.md           # Documentación general del proyecto
├── .env                        # Variables de entorno globales (local)
│
├── auth-service/               # Servicio de Autenticación (Django)
│   ├── Dockerfile              # Imagen del servicio
│   ├── requirements.txt        # Dependencias Python
│   ├── manage.py               # Comandos de Django
│   ├── auth_service/           # Configuración del proyecto Django
│   └── users/                  # App de usuarios (models, views, urls, serializers)
│       ├── migrations/         # Migraciones de la app users
│       └── test_connection.py  # Script para comprobar conexiones a Postgres/Redis
│
├── blog-service/               # Servicio de Blog (placeholder)
│   └── README.md
│
├── email-service/              # Servicio de Email (placeholder)
│   └── README.md
│
├── frontend/                   # Interfaz de Usuario (React) (placeholder)
│   └── README.md
│
└── reverse-proxy/              # Proxy Inverso / API Gateway (placeholder)
    └── README.md
```

## Descripción resumida de componentes

- auth-service/: Servicio Django que gestiona usuarios y autenticación (JWT). Contiene:
  - `Dockerfile`, `requirements.txt`, `manage.py`, aplicación `users` con `models.py`, `views.py`, `urls.py`, `serializers.py`.
  - `test_connection.py` para verificar que Postgres y Redis están accesibles desde el contenedor.

- blog-service/, email-service/, frontend/, reverse-proxy/: Carpetas preparadas para cada microservicio.

## Servicios de soporte (contenedores)

- PostgreSQL (puerto 5432): base de datos relacional utilizada por los servicios.
- Redis (puerto 6379): cache/cola en memoria para sesiones y tareas.

## Cómo levantar el entorno (resumen rápido)

1. Copia el archivo de variables de entorno local (si existe):

```bash
cp .env.example .env
```

2. Construir y levantar los contenedores:

```bash
docker compose up -d --build
```

3. (Dentro del contenedor `auth_service`) Crear migraciones y aplicarlas:

```bash
docker exec -it auth_service python manage.py makemigrations users
docker exec -it auth_service python manage.py migrate
```

4. Crear superusuario (opcional):

```bash
docker exec -it auth_service python manage.py createsuperuser
```

5. Probar conexiones desde el contenedor de auth (script incluido):

```bash
docker exec -it auth_service python test_connection.py
```

## Notas sobre `docker-compose.yml`

- El proyecto incluye servicios `postgres` y `redis` y ahora un servicio `auth` que construye desde `./auth-service`.
- Asegúrate de que las variables de entorno del servicio `auth` (POSTGRES_HOST, REDIS_HOST, etc.) apuntan a los nombres de servicio definidos en `docker-compose.yml`.