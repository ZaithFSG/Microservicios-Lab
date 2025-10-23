# Laboratorio de Microservicios (Django + React)

## Estructura del Proyecto
```
microservices-lab/
├── docker-compose.yml          # Configuración de contenedores y servicios
├── README_GENERAL.md           # Documentación general del proyecto
├── .env                        # Variables de entorno globales
│
├── auth-service/               # Servicio de Autenticación
│   ├── Dockerfile              # Configuración de contenedor
│   ├── requirements.txt        # Dependencias de Python
│   ├── README.md               # Documentación del servicio
│   └── test_conecction.py      # Pruebas de conexión
│
├── blog-service/               # Servicio de Blog
│   └── README.md               # Documentación del servicio
│
├── email-service/              # Servicio de Email
│   └── README.md               # Documentación del servicio
│
├── frontend/                   # Interfaz de Usuario
│   └── README.md               # Documentación del frontend
│
└── reverse-proxy/              # Proxy Inverso / API Gateway
    └── README.md               # Documentación del proxy
```

### Servicios Base
- **PostgreSQL** (Puerto: 5432)
  - Base de datos principal
  - Almacenamiento persistente

- **Redis** (Puerto: 6379)
  - Caché de sesiones
  - Cola de mensajes
  - Almacenamiento en memoria

## Cómo levantar el entorno (Día 1)
1. Copiar `.env.example` a `.env`:
   ```bash
   cp .env.example .env