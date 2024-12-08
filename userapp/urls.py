from django.urls import path
from . import views


urlpatterns = [
    path('', views.user_homepage, name='user_homepage'),  # user homepage
]
