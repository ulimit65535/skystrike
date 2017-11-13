#!/usr/bin/env python
# encoding: utf-8

from ..models import Source, Article
from datetime import datetime
from django import template

register = template.Library()

@register.simple_tag
def get_articles_today(source):
    #article_list = Article.objects.filter(source=source, posted_time__gte=datetime.now().date())
    article_list = Article.objects.filter(source=source)
    return article_list
