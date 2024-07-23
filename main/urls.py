from django.urls import path
from main import views

urlpatterns = [
    path('', views.main, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register')
]