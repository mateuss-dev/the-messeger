from django.urls import path

from . import views

from django.contrib.auth import views as auth_views

app_name = "pages"

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/password_reset_form.html"),
      name='reset_password'),

    path('accounts/password_reset/done/',
     auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"),
      name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"),
      name='password_reset_confirm'),
    
    path('reset_password_complete/',
     auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"),
      name='password_reset_complete'),

]