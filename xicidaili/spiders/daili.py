# -*- coding: utf-8 -*-
import scrapy
from xicidaili.items import *

class DailiSpider(scrapy.Spider):
    name = 'daili'
    allowed_domains = ['www.xicidaili.com']
    start_urls = ['http://www.xicidaili.com/wn/']
    n=1
    def parse(self, response):
        for tr in response.xpath('//tr[@class="odd"]'):
            items=Xici()
            items['ip']=tr.xpath('td[2]/text()').extract_first()
            items['port']=tr.xpath('td[3]/text()').extract_first()
            items['addr'] = tr.xpath('td[4]/a/text()').extract_first()
            items['speed'] = tr.xpath('./td[7]/div/@title').extract_first()
            items['timeout'] = tr.xpath('./td[8]/div/@title').extract_first()
            items['life'] = tr.xpath('td[9]/text()').extract_first()
            items['update'] = tr.xpath('td[10]/text()').extract_first()
            yield items
        next_url = response.xpath('//a[@class="next_page"]/@href').extract()
        self.n=self.n+1
        if next_url:
            # next_url = 'https://movie.douban.com/top250' + next_url[0]
            if self.n<=1:
                yield response.follow(next_url[0])#用response.follow代替request可以不用完整url。
            
