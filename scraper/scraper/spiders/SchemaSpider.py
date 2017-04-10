# -*- coding: utf-8 -*-
"""
Microdata Spider
"""
from scrapy import Request
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from extruct.w3cmicrodata import MicrodataExtractor
from extruct.jsonld import JsonLdExtractor

from scraper.spiders import FastAppsCrawlSpider


class SchemaSpider(FastAppsCrawlSpider):
    name = "schema"
    rules = (
        Rule(LinkExtractor(allow=r'.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        items = []
        def microdata2jsonld(md):
            if md.get('properties'):
                item = md['properties']
                item['@type'] = md.get('type')
                return item
        items += map(microdata2jsonld, MicrodataExtractor().extract(
            response.body_as_unicode(), response.url)['items'])
        items += JsonLdExtractor().extract(
            response.body_as_unicode(), response.url)['items']

        if not items:
            self.logger.debug("No Microdata items found for %s", response.url)

        self.logger.debug("Checking URL for item: %s" , items)

        for item in items:
            if not item or not item.get('url'):
                self.logger.debug("No URL for item: %s" , item)
                continue

            if item['url'] != response.url:
                self.logger.debug("Not in main URL, go there..")
                yield Request(item['url'], callback=self.parse_item)
            else:
                item['@type'] = item.get('type')
                self.logger.debug("Parsed microdata: %s" % item)
                yield item
