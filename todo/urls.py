from django.urls import path, include
from todo import views 


urlpatterns =[
  path('create-todo/', views.CreateTodo.as_view()),
  path('todo/<int:pk>/', views.RetrieveUpdateTodo.as_view()),
  path('todos/', views.ListTodos.as_view()),
]