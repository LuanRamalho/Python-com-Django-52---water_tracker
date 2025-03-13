from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_water_consumption, name='add_water_consumption'),
    path('chart/', views.water_consumption_chart, name='water_consumption_chart'),
    path('list/', views.water_consumption_list, name='water_consumption_list'),
    path('edit/<int:pk>/', views.edit_water_consumption, name='edit_water_consumption'),
    path('delete/<int:pk>/', views.delete_water_consumption, name='delete_water_consumption'),
    path('grafico/', views.grafico_page, name='grafico_page')
]
