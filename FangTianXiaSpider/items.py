# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewHouseFangItem(scrapy.Item):
    collections = "new_house_fang"
    table = "new_house_fang"
    # 省份
    province = scrapy.Field()
    # 市
    city = scrapy.Field()
    # 小区名
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 几居几室
    rooms = scrapy.Field()
    # 面积
    area = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 行政区
    district = scrapy.Field()
    # 是否在销售中
    sale = scrapy.Field()
    # 原url地址
    origin_url = scrapy.Field()


class EsfFangItem(scrapy.Item):
    collections = "esf_fang"
    table = "esf_fang"
    # 省份
    province = scrapy.Field()
    # 市
    city = scrapy.Field()
    # 小区名
    name = scrapy.Field()
    # 几室几厅
    rooms = scrapy.Field()
    # 楼层
    floor = scrapy.Field()
    # 朝向
    toward = scrapy.Field()
    # 建筑年代
    year = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 建筑面积
    area = scrapy.Field()
    # 总价
    price_total = scrapy.Field()
    # 单价
    price_unit = scrapy.Field()
    # 原url地址
    origin_url = scrapy.Field()
