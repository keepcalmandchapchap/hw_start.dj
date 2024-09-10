from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.DecimalField(decimal_places=1, max_digits=3)
    created_at = models.DateTimeField(auto_now_add=True)
