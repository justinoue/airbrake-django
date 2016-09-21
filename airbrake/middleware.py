from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.utils.deprecation import MiddlewareMixin
from airbrake.utils.client import Client

class AirbrakeNotifierMiddleware(MiddlewareMixin):
    def __init__(self):
        self.client = Client()

    def process_exception(self, request, exception):
        if hasattr(settings, 'AIRBRAKE') and not settings.AIRBRAKE.get('DISABLE', False):
            self.client.notify(exception=exception, request=request)
