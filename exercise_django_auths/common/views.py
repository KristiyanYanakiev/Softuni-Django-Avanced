from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView


class HomeView(LoginRequiredMixin, TemplateView):

    print(get_user_model())


# @login_required
# def home_fb(request: HttpRequest) -> HttpResponse:
#     return render(request, 'home.html')

class UserDetailsPage(TemplateView):
    template_name = 'accounts/user_details.html'