from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blue', include('apps.blue.urls')),
    path('green', include('apps.green.urls')),
]
