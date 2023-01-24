from django.urls import path
from . import views

urlpatterns = [
    path('', views.example, name='front_page'),
]
    