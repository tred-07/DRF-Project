from django.shortcuts import render
from .serializers import ReviewSerializer
from rest_framework import viewsets
from .models import Review

# Create your views here.


class ReviewViewsets(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer