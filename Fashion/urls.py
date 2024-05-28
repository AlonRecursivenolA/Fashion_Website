import static
from django.urls import path
from django.conf.urls.static import static

from Fashion import views
from django.contrib.auth.views import LoginView

from django.conf import settings


urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('accounts/profile', views.profile,name="profile")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
