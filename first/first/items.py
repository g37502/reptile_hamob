# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Hamob(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()

class Hamob1(scrapy.Item):
    # title = scrapy.Field()
    url = scrapy.Field()
    body=scrapy.Field()
    type=scrapy.Field()
class Hamob_Img(scrapy.Item):
    url=scrapy.Field()
    body=scrapy.Field()
    type=scrapy.Field()

