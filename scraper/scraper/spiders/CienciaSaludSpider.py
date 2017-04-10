# -*- coding: utf-8 -*-
"""
Master Spider
"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraper.items import NewsArticleItem
from scraper.spiders import FastAppsCrawlSpider


class CienciaSaludSpider(FastAppsCrawlSpider):
    name = "cienciasalud"
    allowed_domains = ["www.cienciasalud.com.mx"]
    start_urls = ['http://www.cienciasalud.com.mx/']

    rules = (
        Rule(LinkExtractor(allow=r'^.+/[^\./]+/[^\./]+$'), callback='parse_article'),
        Rule(LinkExtractor(allow=r'^.+/[^\./]+$'), follow=True),
    )

    def parse_article(self, response):
        self.logger.debug('Page: %s', response.url)
        item = NewsArticleItem()
        item["url"] = response.url
        item["headline"] = response.xpath("normalize-space(//h1[@id='parent-fieldname-title'])").extract()
        item["headline"] = response.xpath("normalize-space(//h1[@id='parent-fieldname-title'])").extract()
        item['@type'] = 'NewsArticle'
        return item
