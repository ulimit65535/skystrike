# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from django.db.utils import IntegrityError


class MyscrapyPipeline(object):
    def process_item(self, item, spider):
        try:
            item.save()
        except IntegrityError:
            print("Duplicate Item")
        return item
