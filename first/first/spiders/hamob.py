import scrapy
from first.items import Hamob

class HamobSpider(scrapy.Spider):
    name = 'hamob'
    allowed_domains = ['www.hamob.com']
    start_urls = ['http://www.hamob.com/']

    def parse(self, response):

        content = response.xpath('/html/body/table//tr/td/table[2]//tr/td[1]/table[1]//tr[1]/td/table//tr/td/text()').extract()

        item = Hamob()
        item['content'] = content
        yield item


