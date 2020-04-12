import os
import sys

from sqlalchemy.exc import InvalidRequestError, IntegrityError

url = "https://www.kuaidaili.com/free/inha/"

import requests
from bs4 import BeautifulSoup
from lxml import html
from apis import db
from apis.models import RawProxy

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

try:
    response = requests.get(url, timeout=10, )
    if response.status_code == 200:
        html = response.text
except requests.RequestException:
    pass


def parse():
    soup = BeautifulSoup(html, "lxml")
    result = soup.find('table', class_='table table-bordered table-striped')
    for item in result.tbody.find_all('tr'):
        ip = item.find('td', attrs={'data-title': 'IP'}).string
        port = item.find('td', attrs={'data-title': 'PORT'}).string
        _type = item.find('td', attrs={'data-title': '匿名度'}).string
        protocol = item.find('td', attrs={'data-title': '类型'}).string
        server_area = item.find('td', attrs={'data-title': '位置'}).string
        res_time = item.find('td', attrs={'data-title': '响应速度'}).string.replace('秒', '')
        last_confirm = item.find('td', attrs={'data-title': '最后验证时间'}).string
        ip_port = ip + ':' + port

        ip_record = RawProxy(ip_port=ip_port, type=_type, server_area=server_area, res_time=float(res_time),
                             last_confirm=last_confirm, protocol=protocol)
        try:

            db.session.add(ip_record)
            db.session.commit()
        except IntegrityError:
            pass
        except InvalidRequestError:
            pass


parse()
