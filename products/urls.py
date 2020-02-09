from django.urls import path
from. import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('sala', views.sala),
    path('eletronicos', views.eletronicos),
    path('limpeza', views.limpeza),
    path('quarto', views.quarto),
    path('banheiro', views.banheiro),
    path('capacetes', views.capacetes),
    path('acampamento', views.acamp),
    path('cozinha', views.cozinha)
    ]