from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from accounts import views
from accounts.views import UserRegister, CustomLogoutView
from common.views import UserDetailsPage

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_fbv, name='login'),
    path('low_level_login/', views.low_level_login_view, name='low-level-login'),
    path('low_level_logout/', views.low_level_logout_view, name='low-level-logout'),
    path('logout/', views.logout_fbv, name='logout'),
    path('register/', views.register_fbv, name='register'),
    path('login_cbv/', LoginView.as_view(template_name='accounts/fbv_views/login_fbv.html'), name='login_cbv'),
    path('logout_cbv/', CustomLogoutView.as_view(), name='logout_cbv'),
    path('details/', UserDetailsPage.as_view(), name='details'),
    path('register-cbv/', UserRegister.as_view(), name='register-cbv'),
    path('password-reset', PasswordResetView.as_view(template_name='accounts/cbv_views/password-reset.html', email_template_name='accounts/cbv_views/password-reset-confirm.html', success_url=reverse_lazy('accounts:password_reset_done')), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='accounts/cbv_views/password-reset-done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='accounts/cbv_views/password-reset-confirm.html'), name='password-reset-confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='accounts/cbv_views/password-reset-complete.html'), name='password-reset-complete'),
    # 1. The password modification form
    path('password-change/',PasswordChangeView.as_view(
             template_name='accounts/cbv_views/password-change.html',
             success_url=reverse_lazy('accounts:password-change-done')
         ),
         name='password-change'),

    # 2. Confirmation page
    path('password-change/done/',PasswordChangeDoneView.as_view(template_name='accounts/cbv_views/password-change-done.html'),
         name='password-change-done'),



]