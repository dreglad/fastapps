# -*- coding: utf-8 -*-

from scrapy.spiders import XMLFeedSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy import Item, Field

from scraper.items import NewsArticleItem


class NITFSpider(XMLFeedSpider):
    name = 'NITFSPider'
    allowed_domains = ['www.jornada.unam.mx']
    start_urls = ['http://www.jornada.unam.mx/rss/politica.xml?v=1']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))

        item = NewsArticleItem()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item
