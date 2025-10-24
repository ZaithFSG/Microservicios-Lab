FROM python:3.11-slim

WORKDIR /app

# instalar dependencias necesarias (libpq-dev para psycopg2 si fuera necesario)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copiar todo para facilitar editar test_connection.py localmente
COPY . .

# mantener el contenedor en ejecución para ejecutar tests con docker exec
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]