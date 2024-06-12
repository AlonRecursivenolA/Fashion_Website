from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
import json
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from . serializer import *
from rest_framework import generics
from .models import Product


from Fashion.models import Product


# Create your views here.

from rest_framework import viewsets
from .serializer import MyModelSerializer
class MyModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = MyModelSerializer


class ViewProducts(ListView):

    model = Product
    template_name = 'products.html'

    def get_queryset(self):
        category = self.request.GET.get('id')  # Assuming user inputs category ID via GET parameter
        print(category)
        queryset = super().get_queryset()
        if category:
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.request.GET.get('category')  # Pass the category ID to the context
        return context


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')



# def index(request):
#     return render(request,template_name='index.html',context={})


def login(request):
    return render(request, template_name='registration/login.html', context={})

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('index')

def profile(request):
    return HttpResponseRedirect(reverse('index'))


