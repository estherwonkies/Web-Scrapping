# -*- coding: utf-8 -*-
import scrapy
import requests
import re


class HpquotesSpider(scrapy.Spider):
    name = 'hpquotes'
    allowed_domains = ['http://www.mugglenet.com/harry-potter/quotes-harry-potter']
    start_urls = ['http://www.mugglenet.com/harry-potter/quotes-harry-potter/']

    def parse(self, response):
        for quotes in response.xpath('//*[@id="page"]/div/div/div/section/div[2]/article/div/div'):
            yield {
                'character' : quotes.css('div.su-spoiler-title::text').extract()
                }
            for quote in quotes.css('div.su-spoiler-title'):
                yield {
                    'responder' : quote.css('em::text').extract()
                        'text' : quote.css('p::text').extract()
                        }


