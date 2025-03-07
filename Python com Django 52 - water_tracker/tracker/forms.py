from django import forms
from .models import WaterConsumption

class WaterConsumptionForm(forms.ModelForm):
    class Meta:
        model = WaterConsumption
        fields = ['date', 'liters']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
