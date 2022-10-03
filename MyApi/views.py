from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class SingerView(ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongView(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
