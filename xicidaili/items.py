# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Xici(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ip=scrapy.Field()
    port=scrapy.Field()
    addr=scrapy.Field()
    speed=scrapy.Field()
    timeout=scrapy.Field()
    life=scrapy.Field()
    update=scrapy.Field()


    pass
