# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class JianshuItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    '''
    解析处理哪些数据，在items.py中定义好
    '''
    title = Field()
    # author =Field()
    url = Field()
    # readNum = Field()
    # commentNum = Field()
    # likeNum = Field()

