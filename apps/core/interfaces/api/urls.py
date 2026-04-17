# apps/core/interfaces/api/urls.py

from django.urls import path
from .views import InfoView

urlpatterns = [
    path('info', InfoView.as_view()),
]
