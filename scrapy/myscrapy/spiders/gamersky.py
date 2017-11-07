#!/usr/bin/env python
# encoding: utf-8

import scrapy
import re
import sys
from datetime import datetime
from myscrapy.items import ArticleItem
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
        article = ArticleItem()

        sel = response.css('div.Mid2L_tit')
        article['title'] = sel.xpath("./*[self::h1]/text()").extract_first()
        detail = sel.css("div.detail").extract_first()
        author_list = re.findall(r"作者：(.+?) ", detail)
        article['author'] = author_list[0] if len(author_list) > 0 else None
        posted_time_list = re.findall(r"    (.+?)来源", detail)

        sel = response.css('div.Mid2L_con')
        article['body'] = sel.extract_first()
        article['first_pic_url'] = sel.xpath('//img/@src').extract_first()

        article['posted_time'] = datetime.strptime(posted_time_list[0].strip(),'%Y-%m-%d %H:%M:%S') if len(posted_time_list) > 0 else None
        article['collected_time'] = datetime.now()
        article['url'] = response.url
        article['source'] = Source.objects.get(name=self.name)
        yield article

