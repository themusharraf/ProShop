from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, CreateView, UpdateView, DeleteView


# Create your views here.
class Index(TemplateView):
    template_name = 'product/product-grid.html'


class Detail(TemplateView):
    template_name = 'product/product-details.html'
