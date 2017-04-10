"""Scraper pipelines"""
# -*- coding: utf-8 -*-
import logging
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):
    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        if not item.get('url'):
            valid = False
            logging.info('Dropping object without identifier')
            raise DropItem("Object Without identifier {0}!".format(item))
    
        self.collection.update({'url': item['url']}, dict(item), upsert=True)
        logging.debug("Object added to database")
        return item
