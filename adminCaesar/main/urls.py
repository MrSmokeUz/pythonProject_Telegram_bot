from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main/index'),  # Главная страница
    # path('about/', views.about, name='about'),  # О сайте
    path('caesar/', views.caesar, name='main/caesar'),
    path('aes/', views.aes, name='main/aes'),
    path('rsa/', views.rsa, name='main/rsa'),
    path('blowfish/', views.caesar, name='main/blowfish'),
    path('test/', views.test,name='main/test')

]
