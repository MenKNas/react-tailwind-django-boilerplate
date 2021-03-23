from django.urls import include, path
from .views import BookAPIView
from todos.views import ListTodo, DetailTodo

urlpatterns = [
    path('todos/', ListTodo.as_view()),
    path('todos/<int:pk>/', DetailTodo.as_view()),
    path('', BookAPIView.as_view()),

]
