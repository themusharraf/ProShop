from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView
from apps.models import Product


# Create your views here.
class Index(ListView):
    model = Product
    template_name = 'product/product-grid.html'


class Detail(DetailView):
    model = Product
    template_name = 'product/product-details.html'
