from django.shortcuts import render
from rest_framework import viewsets          
from .serializers import TodoSerializer     
from .models import Todo        
from rest_framework import generics             

class TodoView(viewsets.ModelViewSet):      
    serializer_class = TodoSerializer          
    queryset = Todo.objects.all()      

class DetailTodo(generics.RetrieveAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    
