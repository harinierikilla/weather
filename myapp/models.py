from django.db import models

# Create your models here.
from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    avg_temp = models.FloatField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    dominant_condition = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} - {self.date} Weather Summary"

