from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import ListTodo, DetailTodo, CreateTodo, UpdateTodo, DeleteTodo, CustomLoginView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ListTodo.as_view(), name='todos'),
    path('todo/<int:pk>/', DetailTodo.as_view(), name='todo'),
    path('create-todo/', CreateTodo .as_view(), name='create-todo'),
    path('edit-todo/<int:pk>/', UpdateTodo.as_view(), name='update-todo'),
    path('delete-todo/<int:pk>/', DeleteTodo.as_view(), name='delete-todo'),
]
