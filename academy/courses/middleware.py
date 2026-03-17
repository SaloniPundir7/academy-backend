
import logging

logger = logging.getLogger(__name__)

class RequestLoggerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = request.user if request.user.is_authenticated else "Anonymous"

        logger.info(
            f"Request | User: {user} | Method: {request.method} | Path: {request.path}"
        )

        response = self.get_response(request)

        logger.info(
            f"Response | Status: {response.status_code} | Path: {request.path}"
        )

        return response

    
import time


class ResponseTimeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time

        print("Response Time:", round(duration, 4), "seconds")

        return response
    
class SecurityHeadersMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        response["X-Project"] = "Academy API"
        response["X-Version"] = "1.0"

        return response
    
import uuid


class RequestIDMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        request.request_id = str(uuid.uuid4())

        print("Request ID:", request.request_id)

        response = self.get_response(request)

        response["X-Request-ID"] = request.request_id

        return response
    
