from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main/index'),  # Главная страница
    # path('about/', views.about, name='about'),  # О сайте
    path('main/caesar.html', views.caesar, name='main/caesar'),
    path('main/aes.html', views.aes, name='main/aes'),
    path('main/rsa.html', views.rsa, name='main/rsa'),
    path('main/blowfish.html', views.caesar, name='main/blowfish'),
    path('main/test.html', views.test,name='main/test')

]
