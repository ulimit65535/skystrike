#!/usr/bin/env python
# encoding: utf-8

from scrapy.spiders import BaseSpider
from myscrapy.items import ArticleItem

class GamerskySpider(BaseSpider):

    """Docstring for GamerskySpider. """
    name = "gamersky"
    allowed_domains = ["gamersky.com"]
    start_urls = ["http://www.gamersky.com"]


