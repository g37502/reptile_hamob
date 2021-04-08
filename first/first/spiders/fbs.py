import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from first.items import Hamob1,Hamob_Img

from PIL import Image
from io import BytesIO
from scrapy_redis.spiders import RedisCrawlSpider
import redis
from first.raids_h import rehis_h
from first.config import config_h
import pymysql,time

msyql_19 = pymysql.connect(host=config_h.get_config('Mysql_19','host'),port=config_h.get_int('Mysql_19','port'),user=config_h.get_config('Mysql_19','user'),
password=config_h.get_config('Mysql_19','password'),database=config_h.get_config('Mysql_19','database'))
class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    redis_key = 'sunkey'
    rules = (
        Rule(LinkExtractor(allow=r''), callback='parse_item', follow=True),
        Rule(LinkExtractor(deny_extensions=['mp4'],tags=['img'],attrs='src'),callback='download_jpg',follow=True),
    )

    # def start_requests(self):
    #     print(self.start_url)
    #     # print(self.start_url)
    def parse_item(self, response):
        # url = response.body_as_unicode()
        # print(self.start_urls)
        url =response.url
        print(url)
        item = Hamob1()
        item['url']=url
        item['body']=response.body
        item['type']='text'
        # print(response.body)
        # print(type(response.body))
        # print(item['body'])
        yield item
        # li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        # for li in li_list:
        #     title = li.xpath('./span[3]//text()').extract_first()
        #     # cont_url = 'http://wz.sun0769.com' + li.xpath('./span[3]/a/@href').extract_first()
        #     # print(cont_url)
        #     item = Hamob1()
        #     item['title'] = title
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
            # yield item
    def download_jpg(self,response):
        # print(self.start_urls)
        url = response.url
        orig_image = Image.open(BytesIO(response.body))
        width, height = orig_image.size
        print(url)
        # print(width,height)
        body = response.body
        # print(type(body))
        # print(body)
        item=Hamob_Img()
        item['url']=url
        # print(url)
        item['body']= body
        item['type']='img'
        # item['start_url']=start_urls
        yield item
    def close(self):
        end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        pic_number = rehis_h.hlen(self.domain + ':' + 'img')
        text_number = rehis_h.hlen(self.domain + ':' + 'text')
        video_number = rehis_h.hlen(self.domain + ':' + 'video')
        sql = f'''update business_func_reptile_reg set LasterReptile={end_time},pic_number={pic_number},
                text_number={text_number},video_number={video_number}
                      where url={self.domain}'''
        cursor = msyql_19.cursor()
        cursor.execute(sql)
        cursor.close()
        print('*' * 100)
