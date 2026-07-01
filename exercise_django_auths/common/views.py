from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from requests import HTTPError

from common.decorators import editor_perm_required


class HomeView(LoginRequiredMixin, TemplateView):
    pass


def is_staff(user):
    return user.is_staff


@login_required
# @permission_required('common.change_article')
# @user_passes_test(is_staff)
def home_fb(request):
    user = request.user

    # if  user.is_anonymous or user.has_usable_password():

    if user.groups.filter(name='Editors').exists():
        return HttpResponse('Here is the Editors home page')
    if user.groups.filter(name='Viewers').exists():
        return HttpResponse('Here is the Viewers home page')
    else:
        return HttpResponse('Here is the Standard home page')

    # return HttpResponseForbidden("You cannot access this page")

class UserDetailsPage(TemplateView):
    template_name = 'accounts/user_details.html'

@editor_perm_required('Editors')
def editors_page(request):
    return HttpResponse("Here is the Editors page")

