import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

# Postgre variables
PG_HOST = os.getenv("POSTGRES_HOST", "postgres")
PG_PORT = int(os.getenv("POSTGRES_PORT", 5432))
PG_USER = os.getenv("POSTGRES_USER", "devuser")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "devpass")
PG_DB = os.getenv("POSTGRES_DB", "main_db")

# Redis variables
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

def test_postgres():
    try:
        import psycopg2
        conn = psycopg2.connect(
            host=PG_HOST,
            port=PG_PORT,
            dbname=PG_DB,
            user=PG_USER,
            password=PG_PASS,
            connect_timeout=5
        )
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        res = cur.fetchone()
        cur.close()
        conn.close()
        print("PostgreSQL: conexión OK ->", res)
        return True
    except Exception as e:
        print("PostgreSQL: ERROR ->", e)
        return False

def test_redis():
    try:
        import redis
        r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, socket_connect_timeout=5, socket_timeout=5)
        r.ping()
        print("Redis: conexión OK -> PONG")
        return True
    except Exception as e:
        print("Redis: ERROR ->", e)
        return False

if __name__ == "__main__":
    print("Iniciando pruebas de conexión...")
    pg_ok = False
    redis_ok = False
    # Intentos de conexión
    for attempt in range(6):
        print(f"Intento {attempt+1}/6...")
        pg_ok = test_postgres()
        redis_ok = test_redis()
        if pg_ok and redis_ok:
            break
        time.sleep(3)

    if pg_ok and redis_ok:
        print("Todas las conexiones OK.")
        sys.exit(0)
    else:
        print("Fallo en alguna conexión.")
        sys.exit(1)