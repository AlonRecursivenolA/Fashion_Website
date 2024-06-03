from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView

from Fashion.models import Product


# Create your views here.



class ViewProducts(ListView):

    model = Product
    template_name = 'products.html'

def index(request):
    return render(request,template_name='index.html',context={})


def login(request):
    return render(request, template_name='registration/login.html', context={})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

def profile(request):
    return HttpResponseRedirect(reverse('index'))
