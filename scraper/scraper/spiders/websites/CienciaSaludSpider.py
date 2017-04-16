# -*- coding: utf-8 -*-
"""
Master Spider
"""
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from scraper.items import NewsArticleItem
from scraper.spiders import FastAppsSpider
from scrapy import Request

class CienciaSaludSpider(FastAppsSpider):
    name = "cienciasalud"
    start_urls = [
        'http://www.cienciasalud.com.mx/lo-mas-reciente/'
    ]

    def parse(self, response):
        self.logger.info('Parsing page: %s', response.url)

        # List
        tileItems = response.css("div.tileItem > a::attr(href)").extract()
        if tileItems:
            for item in tileItems:
                yield Request(response.urljoin(item))

        # Article
        articleDiv = response.css("div#page.item")
        if articleDiv.extract_first() is not None:
            heading = articleDiv.css('h1.documentFirstHeading::text').extract_first() or ''
            description = articleDiv.css('div.documentDescription::text').extract_first() or ''
            articleBody = articleDiv.css('#parent-fieldname-text').xpath('.//child::*').extract()
            section = response.css('span#breadcrumbs-1 > a::text').extract_first()
            yield {
              "type": 'NewsArticle',
              'url': response.url,
              'heading': heading.strip(),
              'description': description.strip() or None,
              'articleBody': ' '.join(articleBody),
              'articleSection': section
            }
            # Image
            image = articleDiv.css('div.newsImageContainer img')
            if image:
                yield {
                    'type': 'ImageObject',
                    'associatedArticle': response.url,
                    'url': image.css('::attr(src)').extract_first().replace('image_mini', 'image'),
                    'caption': image.css('::attr(alt)').extract_first()
                }

        # next page
        next_page = response.css("span.next > a::attr(href)").extract_first()
        if next_page is not None:
            yield Request(response.urljoin(next_page))

    #     item = NewsArticleItem()
    #     item["url"] = response.url
    #     item["headline"] = response.xpath("normalize-space(//h1[@id='parent-fieldname-title'])").extract()
    #     item["headline"] = response.xpath("normalize-space(//h1[@id='parent-fieldname-title'])").extract()
    #     item['@type'] = 'NewsArticle'
    #     return item
