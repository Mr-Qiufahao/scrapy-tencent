# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tiebal.items import TiebalItem

class TiebaSpider(CrawlSpider):
    name = 'tieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/f?ie=utf-8&kw=%E7%BE%8E%E5%A5%B3%E5%90%A7']

    rules = (
        Rule(LinkExtractor(allow=r'https://tieba.baidu.com/p/\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = TiebalItem()
        item['page_list'] = response.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href').extract()
        item['image_list'] = response.xpath('//img[@class="BDE_Image"]/@src').extract()


        yield item

