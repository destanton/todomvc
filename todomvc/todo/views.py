from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todo.models import Todo
from todo.serializers import SpecialSerializer


class TodoListAPIView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = SpecialSerializer


class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = SpecialSerializer
