from django.urls import path
import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('admin_login/', views.admin_login_view, name='admin_login'),
    path('user_login/', views.user_login_view, name='user_login'),
]
