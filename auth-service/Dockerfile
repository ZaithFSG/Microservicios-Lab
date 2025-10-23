FROM python:3.11-slim

WORKDIR /app

# instalar dependencias necesarias (libpq-dev para psycopg2 si fuera necesario)
RUN apt-get update && apt-get install -y build-essential libpq-dev gcc --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copiar todo para facilitar editar test_connection.py localmente
COPY . .

# mantener el contenedor en ejecución para ejecutar tests con docker exec
CMD ["tail", "-f", "/dev/null"]