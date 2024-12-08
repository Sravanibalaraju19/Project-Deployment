from django.urls import path
from . import views
from .views import register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
]
