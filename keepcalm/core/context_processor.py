from django.conf import settings


def default(request):
    return {
        'template_theme': 'default',
        'template_base': 'default.html',
        'settings': settings
    }

