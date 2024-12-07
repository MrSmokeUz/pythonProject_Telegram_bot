from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    # path('about/', views.about, name='about'),  # О сайте
]
