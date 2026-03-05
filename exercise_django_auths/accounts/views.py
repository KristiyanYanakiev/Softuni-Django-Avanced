from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# Create your views here.

def login_fbv(request: HttpRequest) -> HttpResponse:
    form = AuthenticationForm(request, request.POST or None)

    if request.method == 'POST' and form.is_valid():

        user = form.get_user()
        login(request, user)
        return redirect('common:home')

    return render(request, 'accounts/fbv_views/login_fbv.html', {'form': form} )

def logout_fbv(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        logout(request)
    return redirect('common:home')

def register_fbv(request: HttpRequest) -> HttpResponse:
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('common:home')

    return render(request, 'accounts/fbv_views/register_fbv.html', {'form': form})