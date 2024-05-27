from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

def index(request):
    return render(request,template_name='index.html',context={})


def login(request):
    return render(request, template_name='registration/login.html', context={})


def profile(request):
    return HttpResponseRedirect(reverse('index'))
