from django.urls import path
from measurement.views import SensorView, SingleSensorView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<sensor_id>/', SingleSensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
