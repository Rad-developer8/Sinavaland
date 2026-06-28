from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('host/', views.host, name='host'),
    path('tourist/', views.tourist, name='tourist'),
]
