from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.Add.as_view(), name='add_blue'),
]
