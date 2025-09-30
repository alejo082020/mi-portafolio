from django.urls import path
from . import views

urlpatterns = [
    path("", views.open_list, name="open_list"),
    path("<int:pk>/", views.open_detail, name="open_detail"),
]