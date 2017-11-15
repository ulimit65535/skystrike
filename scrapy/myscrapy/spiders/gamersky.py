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
            if page_url.startswith("http://acg.gamersky.com"):
                yield scrapy.Request(url=page_url, callback=self.parse_article_acg)
            else:
                yield scrapy.Request(url=page_url, callback=self.parse_article)

    def parse_article(self, response):
        article = ArticleItem()
        sel = response.css('div.Mid2L_tit')
        article['title'] = sel.xpath("./*[self::h1]/text()").extract_first()
        detail = sel.css("div.detail").extract_first()
        author_list = re.findall(r"作者：(.+?) ", detail)
        article['author'] = author_list[0] if len(author_list) > 0 else None
        posted_time_list = re.findall(r"    (.+?)来源", detail)
        article['posted_time'] = datetime.strptime(posted_time_list[0].strip(),'%Y-%m-%d %H:%M:%S') if len(posted_time_list) > 0 else None
        article['collected_time'] = datetime.now()
        article['url'] = response.url
        article['source'] = Source.objects.get(name=self.name)

        sel = response.css('div.Mid2L_con')
        article['first_pic_url'] = sel.xpath('//img/@src').extract_first()
        article['body'] = sel.extract_first().replace(sel.css('span.pagecss').extract_first(), "")

        next_pages = sel.xpath("//div[@class='page_css']/a[contains(text(), '下一页')]/@href").extract()
        if next_pages:
            yield scrapy.Request(url=next_pages[0], meta={"article": article}, callback=self.parse_article_next)
        else:
            yield article

    def parse_article_acg(self, response):
        article = ArticleItem()
        sel = response.css('div.MidL_title')
        article['title'] = sel.xpath("./*[self::h1]/text()").extract_first()
        detail = sel.xpath("//div[@class='detail']/span/text()").extract()
        article['posted_time'] = datetime.strptime(detail[0],'%Y-%m-%d %H:%M:%S') if len(detail) > 0 else None
        article['author'] = detail[2].split("：", 1)[1] if len(detail) > 2 else None
        article['collected_time'] = datetime.now()
        article['url'] = response.url
        article['source'] = Source.objects.get(name=self.name)

        sel = response.css('div.MidL_con')
        article['first_pic_url'] = sel.xpath('//img/@src').extract_first()
        article['body'] = sel.extract_first().replace(sel.css('span.pagecss').extract_first(), "")

        next_pages = sel.xpath("//div[@class='page_css']/a[contains(text(), '下一页')]/@href").extract()
        if next_pages:
            yield scrapy.Request(url=next_pages[0], meta={"article": article}, callback=self.parse_article_next)
        else:
            yield article

    def parse_article_next(self, response):
        article = response.meta['article']
        if article['url'].startswith("http://acg.gamersky.com"):
            sel = response.css('div.MidL_con')
        else:
            sel = response.css('div.Mid2L_con')
        article['body'] = article['body'] + sel.extract_first().replace(sel.css('span.pagecss').extract_first(), "")

        next_pages = sel.xpath("//div[@class='page_css']/a[contains(text(), '下一页')]/@href").extract()
        if next_pages:
            yield scrapy.Request(url=next_pages[0], meta={"article": article}, callback=self.parse_article_next)
        else:
            yield article

