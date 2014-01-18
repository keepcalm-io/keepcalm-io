from django.conf import settings


def default(request):
    """
    :type request: HttpRequest
    """
    return {
        'settings': settings
    }

