from django.urls import path
from . import views

urlpatterns = [
    path('feeresult', views.feeresult, name='feeresult'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path("choose", views.choose, name='choose'),
    path('admin', views.admin, name='admin'),
    path('newad', views.newad, name='newad'),
    path('parsec', views.parsec, name='parsec'),
    path('feegen', views.feegen, name='feegen'),
    path('teacher', views.teacher, name='teacher')

]