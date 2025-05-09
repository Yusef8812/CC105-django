from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),  # Use login_view
    path('logout/', views.user_logout, name='logout'),  # Use logout_view
    path('predict/', views.predict, name='predict'),
    path('dashboard/', views.dashboard, name='dashboard'),
]