from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_water_consumption, name='add_water_consumption'),
    path('chart/', views.water_consumption_chart, name='water_consumption_chart'),
]
