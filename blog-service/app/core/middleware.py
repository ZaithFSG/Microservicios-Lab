import time, json, logging

logger = logging.getLogger("uvicorn.access" if False else __name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        elapsed = (time.time()-start)*1000
        log = {
            "method": request.method,
            "path": request.get_full_path(),
            "status": response.status_code,
            "time_ms": round(elapsed,2)
        }
        logger.info(json.dumps(log))
        return response