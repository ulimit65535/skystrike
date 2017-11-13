from django.shortcuts import render

# Create your views here.

from .models import Article,Source
from django.views.generic import ListView, DetailView
from datetime import datetime

class IndexView(ListView):
    template_name = 'warehouse/index.html';
    context_object_name = 'source_list'
    model = Source

    # def get_queryset(self):
        # source_list = Source.objects.all()
        # return source_list

    # def get_context_data(self, **kwargs):
        # """只获取当天的文章"""
        # for source in self.get_queryset():
            # kwargs['article_list_' + source.name] = Article.objects.filter(source=source, posted_time__gte=datetime.now().date())
        # return super(IndexView, self).get_context_data(**kwargs)

class ArticleView(DetailView):
    template_name = 'warehouse/single-standard.html'
    context_object_name = 'article'
    model = Article

