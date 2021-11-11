from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView

from .serializers import TodoSerializer
from .models import Todo

class CreateTodo(CreateAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer


class RetrieveUpdateTodo(RetrieveUpdateDestroyAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer

class ListTodos(ListAPIView):
  
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer