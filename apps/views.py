from django.shortcuts import render
from django.views.generic import DetailView, TemplateView


# Create your views here.
class Index(TemplateView):
    template_name = 'index.html'


class Detail(TemplateView):
    template_name = 'detail.html'
