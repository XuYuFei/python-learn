# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 定义获取名人名言文字信息
    text = scrapy.Field()
    # 定义获取的作者
    author = scrapy.Field()
    # 定义获取的标签
    tags = scrapy.Field()

    pass
