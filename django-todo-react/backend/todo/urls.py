from django.urls import path
from .views import TodoView, DetailTodo

urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', TodoView.as_view()),
]
