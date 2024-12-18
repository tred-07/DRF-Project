from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AdvertiseSerializer
from .models import Advertise
from rest_framework import response,status
# Create your views here.

class AdvertiseViewset(viewsets.ModelViewSet):
    queryset=Advertise.objects.all()
    serializer_class=AdvertiseSerializer


