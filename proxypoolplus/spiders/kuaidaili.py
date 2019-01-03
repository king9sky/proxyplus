# -*- coding: utf-8 -*-
import scrapy
from ..items import ProxypoolplusItem


class KuaidailiSpider(scrapy.Spider):
    name = 'kuaidaili'
    allowed_domains = ['www.kuaidaili.com']
    start_urls = ['https://www.kuaidaili.com/free/inha/1/']

    def parse(self, response):

        print(response.url)
        # 正则方式
        # html = response.text
        # import re
        # ip_adress = re.compile(
        #     '<td data-title="IP">(.*)</td>\s*<td data-title="PORT">(\w+)</td>'
        # )
        # re_ip_adress = ip_adress.findall(str(html))
        # for adress, port in re_ip_adress:
        #     result = adress + ':' + port
        #     print(result)
        # xpath
        item_list = response.xpath('//tbody/tr')
        for item in item_list:
            ip = item.xpath('td[@data-title="IP"]/text()').extract_first()
            port = item.xpath('td[@data-title="PORT"]/text()').extract_first()
            result = ip + ':' + port
            print(result)
            yield ProxypoolplusItem(ip=result)

        for i in range(2, 5):
            from scrapy.http import Request
            page = 'https://www.kuaidaili.com/free/inha/{}/'.format(i)
            import time
            time.sleep(2)
            yield Request(url=page, callback=self.parse)

