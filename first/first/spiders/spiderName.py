import scrapy


class SpidernameSpider(scrapy.Spider):
    name = 'spiderName'
    allowed_domains = ['www.hamob.com']
    start_urls = ['http://www.hamob.com/']

    def parse(self, response):
        pass
