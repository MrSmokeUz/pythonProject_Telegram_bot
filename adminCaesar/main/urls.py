from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main/index'),  # Главная страница
    # path('about/', views.about, name='about'),  # О сайте
    path('main/caesar/', views.caesar, name='main/caesar'),
    path('main/aes.html', views.aes, name='main/aes'),
    path('main/rsa.html', views.rsa, name='main/rsa'),
    path('main/blowfish.html', views.blowfish, name='main/blowfish'),
    path('main/test.html', views.test,name='main/test'),
    path('main/vigenere.html', views.vigenere, name='main/viginere'),
    path('main/sha256.html', views.sha, name='main/sha'),
    path('main/otp.html', views.otp, name='main/otp'),
    path('main/des.html', views.des, name='main/des'),
    path('main/3des.html', views.trides, name='main/trides'),
    path('main/md5.html', views.mdfive, name='main/md5'),
]
