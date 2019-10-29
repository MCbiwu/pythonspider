# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector.unified import SelectorList
from qsbk.items import QsbkItem

class QsbkSpiderSpider(scrapy.Spider):
    name = 'qsbk_spider'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://www.lovehhy.net/Joke/Detail/QSBK/2']

    def parse(self, response):
        coon=response.xpath('//div[@id="footzoon"]')
        contents=coon.xpath('.//div[@id="endtext"]/text()').getall()
        for content in contents:
            content=content.strip()
            item=QsbkItem(content=content)
            print(content)
            yield item



