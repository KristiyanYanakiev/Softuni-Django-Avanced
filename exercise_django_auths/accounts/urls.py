from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_fbv, name='login'),
    path('logout/', views.logout_fbv, name='logout'),
    path('register/', views.register_fbv, name='register'),
    path('login_cbv/', LoginView.as_view(template_name='accounts/fbv_views/login_fbv.html'), name='login_cbv'),
    path('logout_cbv/', LogoutView.as_view(), name='logout_cbv')

]