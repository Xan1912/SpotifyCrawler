# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpotifycrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    scrapy.album_name = scrapy.Field()
    scrapy.uri = scrapy.Field()
    scrapy.total_tracks = scrapy.Field()
    pass


# https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF