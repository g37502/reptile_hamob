import redis
import base64
db_conn = redis.StrictRedis(host='112.13.92.136', port=6379, db=0)
#
# with open('C:\\Users\\gaoya\\Desktop\\py2021\\reptile_hamob\\image\\a.jpeg', 'rb') as f:
#     base64_data = base64.b64encode(f.read())
#     print(base64_data)
#     db_conn.set('img', base64_data)

# from urllib.parse import urlparse
# domain = urlparse("https://s.weibo.com/weibo?q=%23%E7%8E%8B%E6%AF%85%E5%A5%89%E5%8A%9D%E6%97%A5%E6%96%B9%E4%B8%8D%E8%A6%81%E6%8A%8A%E6%89%8B%E4%BC%B8%E5%BE%97%E5%A4%AA%E9%95%BF%E4%BA%86%23&from=default#_loginLayer_1617684996631https://s.weibo.com/weibo?q=%23%E7%8E%8B%E6%AF%85%E5%A5%89%E5%8A%9D%E6%97%A5%E6%96%B9%E4%B8%8D%E8%A6%81%E6%8A%8A%E6%89%8B%E4%BC%B8%E5%BE%97%E5%A4%AA%E9%95%BF%E4%BA%86%23&from=default#_loginLayer_1617684996631")
# domain = domain.netloc
# print(type(domain),domain)
# s = domain + ':' + 'text'
# print(s)
# import os
import time

# curren_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
# print("本地当前时间是：", curren_time)

# config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'conf')
# print(config_path)

# s='''SINAGLOBAL=4468578300870.904.1526431935931; _ga=GA1.2.1801914431.1589337272; __gads=ID=99b195e3669bd70b:T=1589337272:S=ALNI_Mbs3yUm6Y7bYeu13PxGzijZSnJa0g; UOR=sports.sina.com.cn,widget.weibo.com,login.sina.com.cn; SCF=AsFiVyGxR57ZLlUzoMLFYDwAyg0K7MEbz_ShyUdYVHpLFQqIkPeSLaIeuWHWP-69UukNNgfQyLmEmre1woKYm40.; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whz6pw9OD92nGnaBGyC1Ozn; SUB=_2AkMXMYfndcPxrAVUnvwXz2vna4pH-jyk5O4RAn7uJhMyOhh77g8fqSVutBF-XKSGEJB5S0KBsdWZN1BKXmZZWux9; _s_tentry=passport.weibo.com; Apache=8106129318175.748.1617758416228; ULV=1617758416308:177:3:2:8106129318175.748.1617758416228:1617673409155; login_sid_t=2ea3158d8007be3c636979a686900426; cross_origin_proto=SSL; WBStorage=8daec78e6a891122|undefined; wb_view_log=1536*8641.25'''
# a='SINAGLOBAL=4468578300870.904.1526431935931; _ga=GA1.2.1801914431.1589337272; __gads=ID=99b195e3669bd70b:T=1589337272:S=ALNI_Mbs3yUm6Y7bYeu13PxGzijZSnJa0g; UOR=sports.sina.com.cn,widget.weibo.com,login.sina.com.cn; SCF=AsFiVyGxR57ZLlUzoMLFYDwAyg0K7MEbz_ShyUdYVHpLFQqIkPeSLaIeuWHWP-69UukNNgfQyLmEmre1woKYm40.; ALF=1649319895; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9Whz6pw9OD92nGnaBGyC1Ozn5JpX5KzhUgL.FoqfSoBEe05fS0M2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcSKqXeoe7SKMN; SUB=_2AkMXMeChdcPxrAVUnvwXz2vna4pH-jyk5IlXAn7uJhIyOhh77m8mqSVutBF-XEtDbqWNHOc7A_1g9OIvzguvxF4b; webim_unReadCount={"time":1617785331825,"dm_pub_total":0,"chat_group_client":0,"chat_group_notice":0,"allcountNum":0,"msgbox":0}; login_sid_t=fe29f1875dd970a4c1fb9e53d0101bee; cross_origin_proto=SSL; WBStorage=8daec78e6a891122|undefined; _s_tentry=-; Apache=429622040971.3225.1617843682743; ULV=1617843682748:178:4:3:429622040971.3225.1617843682743:1617758416308; wb_view_log=1344*8401.25'
# for i in a.split(';'):
#     print(i.split('=',1))
from first.raids_h import rehis_h
s =rehis_h.hget('www.hamob.com:header','cookie')
print(s)
if s:
    s=bytes.decode(s)

    print(type(s))
    e={}
    for i in s.split(';'):
        k,v=i.split('=',1)
        e[k]=v
    print(e)