from django.urls import path

from common.views import HomeView
from common import views

app_name = 'common'

urlpatterns = [
    path('', HomeView.as_view(template_name='home.html'), name='home'),
    path('home-fb', views.home_fb, name='home'),
    path('editors-page', views.editors_page, name='editors-page')

]
