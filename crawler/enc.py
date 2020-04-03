# 西安鲲之鹏网络信息技术有限公司提供的免费代理，也是从其他的地方爬下来的

#http://www.site-digger.com/html/articles/20110516/proxieslist.html
import redis
from requests_html import HTMLSession
session = HTMLSession()
r = session.get('http://www.site-digger.com/html/articles/20110516/proxieslist.html')
conn = redis.ConnectionPool(host='127.0.0.1', port='6379')
db = redis.Redis(connection_pool=conn)


def add_to_redis(full_ip):
    db.hadd('proxies', {full_ip: 100})


def main(r):
    r.html.render()
    trs = r.html.xpath('//tr/td[1]/text()')

    for tr in trs:

        db.sadd('raw_proxy', tr,'1')

        print('正在插入IP',tr)

if __name__ == '__main__':
    main(r)
