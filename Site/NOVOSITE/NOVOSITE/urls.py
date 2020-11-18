
from django.contrib import admin
from django.urls import path
from .view import BoasVindas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Helo/', BoasVindas),
]
