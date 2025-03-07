from django.shortcuts import render, redirect
from .forms import WaterConsumptionForm
import matplotlib.pyplot as plt
from io import BytesIO
from django.http import HttpResponse
from .models import WaterConsumption

def add_water_consumption(request):
    if request.method == 'POST':
        form = WaterConsumptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_water_consumption')
    else:
        form = WaterConsumptionForm()
    return render(request, 'tracker/add_water_consumption.html', {'form': form})

def water_consumption_chart(request):
    # Consultar os dados de consumo
    data = WaterConsumption.objects.all()
    dates = [entry.date for entry in data]
    liters = [entry.liters for entry in data]

    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(dates, liters, marker='o', linestyle='-', color='b')
    plt.title('Consumo de Água ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Litros')
    plt.xticks(rotation=45)

    # Salvar o gráfico em um buffer de memória
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Retornar o gráfico como resposta HTTP
    return HttpResponse(buffer, content_type='image/png')