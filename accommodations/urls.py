from django.urls import path
from . import views

app_name = 'accommodations'

urlpatterns = [
    path('', views.accommodation_list, name='list'),
    path('reserve/<slug:slug>/', views.reserve_accommodation, name='reserve'),
    path('cancel/<slug:slug>/', views.cancel_reservation, name='cancel_reservation'),
    path('my-reservations/', views.my_reservations, name='my_reservations'),
    path('<slug:slug>/', views.accommodation_detail, name='detail'),
]
