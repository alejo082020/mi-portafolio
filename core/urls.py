from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contactame/", views.contactame, name="contactame"),
    path("contacto-exitoso/", views.contacto_exitoso, name="contacto_exitoso"),
    path("test-analytics/", views.test_analytics, name="test_analytics"),
]
