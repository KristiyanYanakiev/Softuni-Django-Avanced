from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import logout_then_login, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from accounts.forms import CustomUserCreationForm


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


def low_level_login_view(request):

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user:
        login(request, user)
        return redirect('common:home')

    return render(request, 'accounts/low_level_login.html')


def low_level_logout_view(request):
    if request.method == 'POST':
        print('here user is logging out')
        print("Before logout", request.user)
        logout(request)
        print("After logout", request.user)
        return redirect('common:home')

    if request.method == "GET":
        return render(request, 'accounts/low_level_logout.html')


class UserRegister(CreateView):

    form_class = CustomUserCreationForm
    template_name = 'accounts/cbv_views/register.html'
    success_url = reverse_lazy('common:home')

    def form_invalid(self, form):
        messages.error(request=self.request, message='Please correct errors below')
        return super().form_invalid(form)

class CustomLogoutView(LoginRequiredMixin, LogoutView):
    http_method_names = ['get', 'post']
    template_name = 'accounts/cbv_views/logout.html'
    next_page = reverse_lazy('accounts:login_cbv')










