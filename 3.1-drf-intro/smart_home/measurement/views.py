# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, PostSensorSerializer, PatchSensorSerializer, MeasurementSerializer, PostMeasurementSerializer

class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        measurements = Measurement.objects.all()
        ser = SensorDetailSerializer(sensors, many=True)
        return Response(ser.data)
    def post(self, request):
        ser = PostSensorSerializer(data=request.data)
        if ser.is_valid():        
            ser.save()
            return Response(status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
    
class SingleSensorView(APIView):
    def get(self, request, sensor_id):
        if sensor_id is not None:
            sensor = Sensor.objects.filter(id=sensor_id).get()
            ser = SensorDetailSerializer(sensor)
            return Response(ser.data)
        else:
            return Response('Сенсора с данным ID не найдено')
    
    def patch(self, request, sensor_id):
        sensor = Sensor.objects.filter(id=sensor_id).get()
        ser = PatchSensorSerializer(sensor, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(f"Сенсор с ID {sensor_id} успешно обновлен")
    

class MeasurementView(APIView):
    def post(self, request):
        ser = PostMeasurementSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


            