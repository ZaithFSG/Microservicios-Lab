class AuthHeaderLogger:
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        auth = request.META.get('HTTP_AUTHORIZATION','')
        if auth:
            # solo loguea; no valida
            import logging
            logging.getLogger("auth").info(f"AuthHeader: {auth[:50]}")
        return self.get_response(request)