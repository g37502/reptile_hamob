# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# from first.first import settings
import redis,re
from first.raids_h import rehis_h
from urllib.parse import urlparse
from first.config import config_h
import pymysql,time

msyql_19 = pymysql.connect(host=config_h.get_config('Mysql_19','host'),port=config_h.get_int('Mysql_19','port'),user=config_h.get_config('Mysql_19','user'),
password=config_h.get_config('Mysql_19','password'),database=config_h.get_config('Mysql_19','database'))
img_list=['mng', 'pct', 'bmp', 'gif', 'jpg', 'jpeg', 'png', 'pst', 'psp', 'tif',
    'tiff', 'ai', 'drw', 'dxf', 'eps', 'ps', 'svg', 'cdr', 'ico',]
class FbsproPipeline(object):
    def process_item(self,item,spider):
        return item

class FirstPipeline:
    fp=None
    def open_spider(self,spider):
        self.fp = open('./hamob.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        # print(type(spider))
        url = item['url']
        # print(title)
        # content = item['content']
        self.fp.write(url+'\n')
        # with open(,'w',)
        return item
    def close_spider(self,spider):
        self.fp.close()
import base64
# host=spider.settings.get('REDIS_HOST',locals)
# port=spider.settings.get('REDIS_PORT',6379)
# db_index=spider.settings.get('REDIS_DB_INDEX',0)
# self.db_conn =redis.StrictRedis(host=host, port=port, db=db_index)
class text(object):
    def open_spider(self,spider):

        # print(spider.start_url,'*'*100)
        pass

    def process_item(self,item,spider):
        url=item['url']
        print(url)
        body=item['body']
        domain = urlparse(spider.start_url).netloc
        type = item['type']
        if type == 'img':
            body = base64.b64encode(body)
            # print('图片',suffix)
            #start_url+img:url:body
            key = domain + ':' + 'img'
            rehis_h.hset(key,url,body)
        elif type == 'text':
            #start_url+text:url:body
            key =domain +':'+'text'
            rehis_h.hset(key,url,body)
    def close_spider(self,spider):
        end_time =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        pic_number=rehis_h.hlen(self.domain+':'+'img')
        text_number=rehis_h.hlen(self.domain+':'+'text')
        video_number = rehis_h.hlen(self.domain+':'+'video')
        sql = f'''update business_func_reptile_reg set LasterReptile={{end_time}},pic_number={pic_number},
        text_number={text_number},video_number={video_number}
              where url={self.domain}'''
        cursor = msyql_19.cursor()
        cursor.execute(sql)
        cursor.close()
        print('*'*100)
from scrapy.pipelines.images import ImagesPipeline
class img(ImagesPipeline):
    pass