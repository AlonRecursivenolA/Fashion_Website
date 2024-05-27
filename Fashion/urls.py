from django.urls import path

from Fashion import views

urlpatterns = [
    path('', views.index, name="index"),

]
