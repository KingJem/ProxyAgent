import os
import sys

url = "https://www.kuaidaili.com/free/inha/"

import requests
from bs4 import BeautifulSoup
from lxml import html
from apis.models import db
from apis.models import RawProxy

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        html = response.text
except requests.RequestException:
    pass

soup = BeautifulSoup(html, "lxml")
result = soup.find('table', class_='table table-bordered table-striped')
for item in result.tbody.find_all('tr'):
    ip = item.find('td', attrs={'data-title': 'IP'}).string
    port = item.find('td', attrs={'data-title': 'PORT'}).string
    _type = '高匿'
    protocol = 'http'
    server_area = item.find('td', attrs={'data-title': '位置'}).string
    res_time = item.find('td', attrs={'data-title': '响应速度'}).string.replace('秒', '')
    last_confirm = item.find('td', attrs={'data-title': '最后验证时间'}).string
    ip_record = RawProxy(ip=ip, port=port, type=1, server_area=server_area, res_time=float(res_time),
                         last_confirm=last_confirm, protocol=protocol)
    db.session.add(ip_record)
    db.session.commit()
