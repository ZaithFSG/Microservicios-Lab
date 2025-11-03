from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db import connections
import redis, os

@api_view(['GET'])
def healthz(request):
    # DB
    try:
        c = connections['default']
        c.cursor()  # will raise if no connection
        db_ok = True
    except Exception:
        db_ok = False
    # Redis
    try:
        r = redis.Redis(host=os.environ.get('REDIS_HOST','redis'), port=int(os.environ.get('REDIS_PORT',6379)), socket_connect_timeout=2)
        r.ping()
        redis_ok = True
    except Exception:
        redis_ok = False
    status = 200 if db_ok and redis_ok else 503
    return Response({"db": db_ok, "redis": redis_ok}, status=status)