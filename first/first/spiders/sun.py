import scrapy
from first.items import Hamob
from scrapy_redis.spiders import RedisCrawlSpider

class SunSpider(scrapy.Spider):
    name = 'sun'
    # allowed_domains = ['http://wz.sun0769.com/political/index/politicsNewest?id=1']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=']
    url = 'http://wz.sun0769.com/political/index/politicsNewest?id=1&page=%d'
    page=2
    def parse(self, response):
        li_list=response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            title= li.xpath('./span[3]//text()').extract_first()
            cont_url = 'http://wz.sun0769.com' + li.xpath('./span[3]/a/@href').extract_first()
            # print(cont_url)
            item = Hamob()
            item['title'] = title
            yield scrapy.Request(cont_url,callback=self.parse_detail,meta={'item':item})
        if self.page <= 5:
            new_url = format(self.url %self.page)
            print(new_url)
            self.page+=1
            yield scrapy.Request(new_url, callback=self.parse)
    def parse_detail(self, response):
        item=response.meta['item']
        content=response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract_first()
        item['content']=content
        yield item

