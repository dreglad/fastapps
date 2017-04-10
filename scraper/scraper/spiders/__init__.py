# -*- coding: utf-8 -*-
"""
Master Spider
"""
from urlparse import urlparse

from scrapy.spiders import BaseSpider


class FastAppsSpider(BaseSpider):
    """
    This spider will try to crawl whatever is passed in `start_urls` which
    should be a comma-separated string of fully qualified URIs.

    Example: start_urls=http://localhost,http://example.com
    """
    def __init__(self, *args, **kwargs):
        super(FastAppsSpider, self).__init__(*args, **kwargs)
        self.logger.debug("FastAppsCrawlSpider __init__")
        if 'start_urls' in kwargs:
            self.start_urls = kwargs.pop('start_urls').split(',')
            self.allowed_domains = [urlparse(url).netloc for url in self.start_urls]

            self.logger.debug("Settings start URLs to: %s", self.start_urls)
