from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Article

def index(request):
    article_list = Article.objects.all().order_by('-collected_time')
    return render(request, 'warehouse/index.html', context={'article_list': article_list})
