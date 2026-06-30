from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import HTTPError


class HomeView(LoginRequiredMixin, TemplateView):
    pass




def home_fb(request):
    user = request.user

    if  user.is_anonymous or user.has_usable_password():
        return render(request, 'home.html')
    return HttpResponseForbidden("You cannot access this page")

class UserDetailsPage(TemplateView):
    template_name = 'accounts/user_details.html'

