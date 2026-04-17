from django.urls import path, include
from apps.core.views import health

urlpatterns = [
    path('', health),
    path('api/', include('apps.core.interfaces.api.urls')),
]
