from django.db import models
from django.utils import timezone

# Create your models here.


class SensorData(models.Model):
    device_id = models.CharField(max_length=100)
    sensor_id = models.CharField(max_length=100)
    sensor_name = models.CharField( max_length=100, default="Unknow sensor")
    value = models.FloatField()
    timestamp = models.DateTimeField( default=timezone.now)

    def __str__(self):
        return f"{self.sensor_name} -  {self.value} at {self.timestamp}"
