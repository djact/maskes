import pytz
from django.utils.timezone import activate

class AdminTimezoneMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(self.process_request(request))
        return response

    @staticmethod
    def process_request(request):
        if request.path.startswith("/admin"):
            activate(pytz.timezone('US/Pacific'))
        return request