# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy
import requests
from scrapy import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

from properties.items import PropertiesItem


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['maoyan.com/board']
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response):
        next_selector = response.xpath('//*[contains(@class, "page_")]/@href')
        for url in next_selector.extract():
            yield Request(urljoin(response.url, url))

    def parse_item(self, response):
        """
        @url https://maoyan.com/board/4
        @returns items1
        @scrapes title url actor date grade_integer grade_fraction image image_url
        :param response: response
        :return: items
        """
        l = ItemLoader(item=PropertiesItem(), response=response)
        l.add_xpath("title", '//*[@class="name"]/a/text()', MapCompose(str.strip))
        l.add_xpath("url", '//*[@class="name"]/a/@href', MapCompose(lambda i: urljoin(response.url, i)))
        l.add_xpath("actor", '//*[@class="star"]/text()', MapCompose(str.strip))
        l.add_xpath("date", '//*[@class="releasetime"]/text()')
        l.add_xpath("grade_integer", '//*[@class="integer"]/text()')
        l.add_xpath("grade_fraction", '//*[@class="fraction"]/text()')
        l.add_xpath("image", '//*[@class="image-link"]/img[2]/@data-src')
        l.add_xpath("image_url", '//*[@class="image-link"]/img[2]/@data-src')
        return l.load_item()
