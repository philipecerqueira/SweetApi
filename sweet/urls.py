from django.contrib import admin
from django.urls import include, path

from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]
