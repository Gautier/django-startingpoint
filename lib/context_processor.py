from django.conf import settings

def context(request):
    base_template = getattr(settings, "BASE_TEMPLATE", "base.html")

    DEBUG = settings.DEBUG
    MEDIA_URL = settings.MEDIA_URL

    return locals()
