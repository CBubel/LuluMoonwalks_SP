"""LuluMoonwalks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from mainsite import views
from django.conf import settings

urlpatterns = [
    path('', views.get_index_page),
    path('index/', views.get_index_page, name="home-page"),
    path('about/', views.get_about_page, name="about-page"),
    path('faq/', views.get_faq_page, name="faq-page"),
    path('contact/', views.get_contact_page, name="contact-page"),
    path('pinatas/', views.get_pinatas_page, name="pinata-page"),
    path('moonwalks/', views.get_moonwalks_page, name="moonwalk-page"),
    path('admin/', admin.site.urls, name="admin-page"),
    path('success-page/', views.get_success_page, name="success-page"),
    path('test/', views.get_test_page, name="test-page")
]
