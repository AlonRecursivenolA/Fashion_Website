from django.urls import path

from Fashion import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('accounts/profile', views.profile,name="profile")
]
