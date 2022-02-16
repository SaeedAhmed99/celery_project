from django.urls import path
from . import views


urlpatterns = [
    path('', views.mass_email)
]
