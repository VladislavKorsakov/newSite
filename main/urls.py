from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.logout_page, name='logout'),
    path('calculation/', views.calculation_page, name='calculation'),
    path('profile/', views.profile_page, name='profile'),
]



