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

urlpatterns = [
    path('', views.get_index_page),
    path('index/', views.get_index_page),
    path('about/', views.get_about_page),
    path('faq/', views.get_faq_page),
    path('contact/', views.get_contact_page),
    path('pricing/', views.get_pricing_page),
    path('pinatas/', views.get_pinatas_page),
    path('moonwalks/', views.get_moonwalks_page),
    path('admin/', admin.site.urls),
]
