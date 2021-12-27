from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get/ajax/update_ping', views.update_ping, name='index'),
]