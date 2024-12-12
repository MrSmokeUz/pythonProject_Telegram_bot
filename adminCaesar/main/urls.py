from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main/index'),  # Главная страница
    # path('about/', views.about, name='about'),  # О сайте
    path('caesar/', views.caesar, name='main/caesar'),

]
