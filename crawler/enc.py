# 西安鲲之鹏网络信息技术有限公司提供的免费代理，也是从其他的地方爬下来的

# http://www.site-digger.com/html/articles/20110516/proxieslist.html
import redis
from requests_html import HTMLSession

session = HTMLSession()
r = session.get('http://www.site-digger.com/html/articles/20110516/proxieslist.html')
from api.app import db
from model import RawProxy



def enc(r):
    r.html.render()
    trs = r.html.xpath('//tr/td[1]/text()')

    for tr in trs:
        ip = RawProxy()




if __name__ == '__main__':
    enc(r)
