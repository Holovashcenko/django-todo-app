from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Todo


class CustomLoginView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todos')


class ListTodo(LoginRequiredMixin, ListView):
    model = Todo
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(user=self.request.user)
        context['count'] = context['todos'].filter(is_completed=False).count()
        return context


class DetailTodo(LoginRequiredMixin, DetailView):
    model = Todo
    context_object_name = 'todo'
    template_name = 'main/todo.html'


class CreateTodo(LoginRequiredMixin, CreateView):
    model = Todo
    fields = {'title', 'description', 'is_completed'}
    success_url = reverse_lazy('todos')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTodo, self).form_valid(form)


class UpdateTodo(LoginRequiredMixin, UpdateView):
    model = Todo
    fields = {'title', 'description', 'is_completed'}
    success_url = reverse_lazy('todos')


class DeleteTodo(LoginRequiredMixin, DeleteView):
    model = Todo
    context_object_name = 'todo'
    success_url = reverse_lazy('todos')
