from django.shortcuts import render
from .models import todos
from .serializers import todosserializer
from rest_framework import viewsets

# Create your views here.



class todosapi(viewsets.ModelViewSet):
    queryset = todos.objects.all()
    serializer_class = todosserializer