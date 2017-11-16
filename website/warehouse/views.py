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
    template_name = 'warehouse/article.html'
    context_object_name = 'article'
    model = Article

class SourceView(ListView):
    template_name = 'warehouse/source.html'
    context_object_name = 'article_list'
    model = Article

