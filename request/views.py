from django.shortcuts import render
from rest_framework import viewsets,views
from .models import Request
from .serializers import RequestSerializer
# Create your views here.

class RequestViewsets(viewsets.ModelViewSet):
    queryset=Request.objects.all()
    serializer_class=RequestSerializer