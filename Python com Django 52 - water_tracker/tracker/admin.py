from django.contrib import admin
from .models import WaterConsumption

@admin.register(WaterConsumption)
class WaterConsumptionAdmin(admin.ModelAdmin):
    list_display = ('date', 'liters')  # Exibe os campos principais na lista
    search_fields = ('date',)  # Permite pesquisar por data
    list_filter = ('date',)  # Adiciona um filtro por data
