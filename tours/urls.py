from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    # fixed paths must come BEFORE the <slug:slug>/ catch-all
    path('my/reservations/', views.my_reservations, name='my_reservations'),
    path('', views.tour_list, name='list'),
    path('<slug:slug>/', views.tour_detail, name='detail'),
    path('<slug:slug>/reserve/', views.reserve_tour, name='reserve'),
    path('<slug:slug>/cancel/', views.cancel_reservation, name='cancel_reservation'),
]
