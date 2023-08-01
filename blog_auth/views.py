from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import UserRegisterForm, UserLoginForm


class Register(CreateView):
    form_class = UserRegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'auth/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogout(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')
