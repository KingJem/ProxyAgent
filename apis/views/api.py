from flask import Blueprint
from sqlalchemy import func

api = Blueprint('api', __name__)

from apis.models import RawProxy
from utils.utils import to_json


@api.route('/')
def index():
    data = {'get': 'return a random ip ',
            'get_all': 'return all useful ips',
            'delete': 'delete ip '}
    return data


@api.route('/get/')
@api.route('/get/<num>/')
def get(num=None):
    """
    return a random proxy
    返回一个随机可用的代理
    """
    if num:

        proxies = RawProxy.query.filter().order_by(func.random()).limit(num).all()
    else:
        proxies = RawProxy.query.filter().order_by(func.random()).limit(1).all()
    if not proxies:
        data = {'code': '404', 'msg': 'proxy not found'}
    else:
        data = {'code': 200, 'msg': 'success', 'proxies': to_json(proxies)}
    return data


@api.route('/get_all/')
def getall():
    proxies = RawProxy.query.all()
    if not proxies:
        data = {'code': '404', 'msg': 'proxy not found'}
    else:
        data = {'code': 200, 'msg': 'success', 'proxies': to_json(proxies)}
    return data


@api.route('/count/')
def status():
    proxies_count = RawProxy.query.count()
    data = {
        'msg': 'success',
        'useful_proxies_count': proxies_count
    }

    return data
