from django.shortcuts import render

# Create your views here.

from .models import Article,Source
from django.views.generic import ListView, DetailView
from datetime import datetime

class IndexView(ListView):
    template_name = 'warehouse/index.html';
    context_object_name = 'source_list'
    model = Source

class ArticleView(DetailView):
    template_name = 'warehouse/single-standard.html'
    context_object_name = 'article'
    model = Article

