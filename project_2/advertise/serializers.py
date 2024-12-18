from rest_framework import serializers
from .models import Advertise
from django.shortcuts import render,HttpResponse
class AdvertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advertise
        # fields=['title','description','contact']
        fields='__all__'