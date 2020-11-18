from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import FoodSerializer
from .models import Food

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.filter(active=True)
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category__name', 'name']
