# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Thing(scrappy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    description = scrapy.Field()
    potentialAction = scrapy.Field()
    image = scrapy.Field()
    isBasedOnUrl = scrapy.Field(help_text='Si aplica, Indica la/las URLs de donde se extrajo la información')
    

class CreativeWork(Thing):
    producer = scrapy.Field()
    author = scrapy.Field()
    headline = scrapy.Field()
    alternativeHeadline = scrapy.Field()
    dateCreated = scrapy.Field()
    datePublished = scrapy.Field()
    dateModified = scrapy.Field()
    text = scrapy.Field()
    thumbnailUrl = scrapy.Field()
    keywords = scrapy.Field()
    contentLocation = scrapy.Field()
    associatedMedia = scrapy.Field()
    interactionCount = scrapy.Field()
    thumbnail = scrapy.Field()
    audio = scrapy.Field()
    image = scrapy.Field()
    video = scrapy.Field()


class NewsArticleItem(CreativeWork):
    articleBody = scrapy.Field()
    articleSection = scrapy.Field()
    printEdition = scrapy.Field()
    wordCount = scrapy.Field()


class VisualArtwork(CreativeWork):
    artform = scrapy.Field()


class MediaObject(CreativeWork):
    embedURL = scrapy.Field()
    contentURL = scrapy.Field()
    fileFormat = scrapy.Field()
    width = scrapy.Field()
    height = scrapy.Field()
    contentSize = scrapy.Field()
    duration = scrapy.Field()
    bitrate = scrapy.Field()
    encodesCreativeWork = scrapy.Field()


class VideoObject(MediaObject):
    caption = scrapy.Field()
    transcript = scrapy.Field()
    videoQuality = scrapy.Field()


class ImageObject(MediaObject):
    caption = scrapy.Field()
    exifData = scrapy.Field()
    transcript = scrapy.Field()
    videoQuality = scrapy.Field()


class Clip(CreativeWork):
    partOfEpisode = scrapy.Field()


class CreativeWorkSeries(CreativeWork):
    startDate = scrapy.Field()
    endDate = scrapy.Field()
    numberOfEpisodes = scrapy.Field()


class Blog(CreativeWork):
    pass


class Episode(CreativeWork):
    partOfSeries = scrapy.Field()
    episodeNumber = scrapy.Field()
    caption = scrapy.Field()
    partOfSeries = scrapy.Field()


class ItemList(MediaObject):
    itemListElement = scrapy.Field()
    numberOfItems = scrapy.Field()
    itemListOrder = scrapy.Field()


class ListItem(MediaObject):
    item = scrapy.Field()
    nextItem = scrapy.Field()
    position = scrapy.Field()
    previousItem = scrapy.Field()
