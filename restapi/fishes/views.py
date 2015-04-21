from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from fishes.models import Fish
from fishes.serializers import FishSerializer

# Create your views here.
class FishViewSet(viewsets.ModelViewSet):
    queryset = Fish.objects.all()
    serializer_class = FishSerializer
