# -*- coding: utf-8 -*-
import scrapy


class YundailiSpider(scrapy.Spider):
    name = 'yundaili'
    allowed_domains = ['www.ip3366.net']
    start_urls = ['http://http://www.ip3366.net/free/?stype=1&page=1']

    def parse(self, response):
        pass

