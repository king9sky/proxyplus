# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxypoolplusPipeline(object):

    def __init__(self):
        self.f = None
        #修改1
        #dev修改
        #开发新功能到一半
        #开发另一半功能
        #新增功能

    def process_item(self, item, spider):
        '''
        2,如果没有rom_crawler,则obj=类（）
        :param item: 爬虫中yield的对象
        :param spider: 爬虫对象
        :return:
        '''
        print(item.items)
        self.f.write(str(item) + '\n')
        return item

    # @classmethod
    # def from_crawler(cls, crawler):
    #     """
    #     1。检测是否有此方法，如果有obj=类.from_crawler()
    #     初始化时候，用于创建pipeline对象
    #     :param crawler:
    #     :return:
    #     """
    #     # val = crawler.settings.getint('MMMM') #从配置文件里拿数据：例如数据库账号信息
    #     return cls(val)

    def open_spider(self, spider):
        """
        3，爬虫开始执行时，调用
        :param spider:
        :return:
        """
        self.f = open('news.log', 'a', encoding='utf-8')
        print('000000')

    def close_spider(self, spider):
        """
        4，爬虫关闭时，被调用
        :param spider:
        :return:
        """
        self.f.close()
        print('111111')
