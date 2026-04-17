# apps/core/interfaces/api/views.py

import sys
import platform
import django
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

class InfoView(APIView):
    def get(self, request):
        return Response({
            "python_version": sys.version,
            "django_version": django.get_version(),
            "environment": {
                "debug": settings.DEBUG,
                "allowed_hosts": settings.ALLOWED_HOSTS,
            },
            "system": {
                "platform": platform.system(),
                "platform_release": platform.release(),
            }
        })
