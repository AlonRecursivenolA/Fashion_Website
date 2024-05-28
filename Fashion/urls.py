import static
from django.urls import path
from django.conf.urls.static import static

from Fashion import views
from django.contrib.auth.views import LoginView

from django.conf import settings

from Fashion.views import SignUpView

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('accounts/profile', views.profile,name="profile"),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
