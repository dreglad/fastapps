# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Item, Field


class NewsArticleItem(Item):
    """https://schema.org/NewsArticle"""
    headline = Field()
    url = Field()    


class HomeSpider(CrawlSpider):
    name = "home"
    allowed_domains = ["www.cienciasalud.com.mx"]
    start_urls = ['http://www.cienciasalud.com.mx/']

    rules = (
        Rule(LinkExtractor(allow=r'/[^\./]+/?$')),
        Rule(LinkExtractor(allow=r'/[^\./]+/[^\./]+/?$'), callback='parse_article'),
    )

    def parse_article(self, response):
        self.logger.info('Item page: %s', response.url)

        item = NewsArticleItem()
        item["url"] = response.url
        item["headline"] = response.xpath("normalize-space(//h1[@id='parent-fieldname-title'])").extract()
        item["headline"] = response.xpath("normalize-space(//h1[@id='parent-fieldname-title'])").extract()

        parent-fieldname-text
        return item
