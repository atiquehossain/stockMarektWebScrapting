# financeApp/models.py
from django.db import models

class HistoricalData(models.Model):
    date = models.DateField(unique=True)
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.BigIntegerField()

    def __str__(self):
        return f"{self.date}: {self.close}"
