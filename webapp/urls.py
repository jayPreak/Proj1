from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.index, name='add')
]