"""Scraper pipelines"""
# -*- coding: utf-8 -*-
import logging
import pymongo

from scrapy.conf import settings
from scrapy.exceptions import DropItem


from arango import ArangoClient


class ArangoDBPipeline(object):
    def __init__(self):
        client = ArangoClient(
            protocol='http',
            host='localhost',
            port=8529,
            username='root',
            password='',
            enable_logging=True
        )
        self.db = client.db('fastapps')

        self.isPartOf = 'WebSite/CienciaSalud'

    def process_item(self, item, spider):
        if not item.get('url'):
            logging.info('Dropping object without identifier')
            raise DropItem("Object Without identifier {0}!".format(item))

        itemType = item.get('type')
        del item['type']

        item.update({
            'isPartOf': self.isPartOf,
            '_id': item.get('url')
        })

        self.db.collection(itemType).insert(item)
        logging.info("Object added to database")
        return item


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
        logging.info("Object added to database")
        return item
