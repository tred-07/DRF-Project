from django.shortcuts import render,HttpResponse
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from .serializers import AdvertiseSerializer
from .models import Advertise
# Create your views here.

class AdvertiseViewsets(ModelViewSet):
    queryset=Advertise.objects.all()
    serializer_class=AdvertiseSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        print(self.request.query_params)
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
