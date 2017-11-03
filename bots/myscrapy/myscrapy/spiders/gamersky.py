#!/usr/bin/env python
# encoding: utf-8

import scrapy
from datetime import datetime
from myscrapy.items import ArticleItem, SourceItem
from warehouse.models import Source


class GamerskySpider(scrapy.Spider):

    """Docstring for GamerskySpider. """
    name = "gamersky"
    allowed_domains = ["gamersky.com"]
    start_urls = ["http://www.gamersky.com"]

    def parse(self, response):
        page_xpath = "//div[@class='Mid1Mcon block']/ul[@class='Ptxt block']/li/div/a[font[contains(@class, 'tc')]]/@href"
        for page_url in response.xpath(page_xpath).extract():
            yield scrapy.Request(url=page_url, callback=self.parse_article)

    def parse_article(self, response):
        source = Source()
        source.name = self.name
        source.url = self.start_urls[0]

        article = ArticleItem()
        article['title'] = "111"
        article['body'] = "222"
        article['author'] = "333"
        article['posted_time'] = datetime.now()
        article['collected_time'] = datetime.now()
        article['source'] = source
        #yield article
        article.save()

