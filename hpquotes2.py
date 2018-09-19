# -*- coding: utf-8 -*-
import scrapy
import requests


class hpquotes2Spider(scrapy.Spider):
    name = 'hpquotes2'
    start_urls = ['http://tomfeltonandmore.tripod.com/home/id9.html']

    def parse(self, response):
        for quotes in response.xpath('/html/body/table/tbody/tr/td[3]/table[2]/tbody/tr[1]/td/div[1]'):
            yield response.css('p.MsoNormal::text').extract()