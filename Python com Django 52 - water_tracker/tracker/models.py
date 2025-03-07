from django.db import models

class WaterConsumption(models.Model):
    date = models.DateField()
    liters = models.FloatField()

    def __str__(self):
        return f"{self.date} - {self.liters} L"
