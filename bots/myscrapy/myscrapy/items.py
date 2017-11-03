# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from warehouse.models import Article, Source


class ArticleItem(DjangoItem):
    django_model = Article

class SourceItem(DjangoItem):
    django_model = Source
