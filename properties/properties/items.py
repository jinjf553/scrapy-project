# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field, Item


class PropertiesItem(Item):
    title = Field()
    url = Field()
    actor = Field()
    date = Field()
    grade_integer = Field()
    grade_fraction = Field()
    image_url = Field()
    image = Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
