import os
import sys

from flask import Blueprint
from sqlalchemy import func

from utils.utils import to_json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

from apis.models import RawProxy

tag_bp = Blueprint('tag', __name__)


@tag_bp.route("/tag/<protocol>/all/")
@tag_bp.route("/tags/<protocol>/<_type>/all/")
@tag_bp.route("/tags/<protocol>/<_type>/<num>")
def muti_tags(protocol, _type=None, num=None):
    if not num:
        if not _type:
            proxies = RawProxy.query.filter(RawProxy.protocol == protocol).all()
            if not proxies:
                data = {'code': '404', 'msg': 'proxy not found'}
            else:
                data = {'code': 200, 'msg': 'success'}
            return data

        else:
            proxies = RawProxy.query.filter(RawProxy.protocol == protocol, RawProxy.type == _type).all()
            if not proxies:
                data = {'code': '404', 'msg': 'proxy not found'}
            else:
                data = {'code': 200, 'msg': 'success', 'proxies': to_json(proxies)}
            return data
    else:
        proxies = RawProxy.query.filter(RawProxy.protocol == protocol, RawProxy.type == _type).order_by(
            func.random()).limit(num).all()
        if not proxies:
            data = {'code': '404', 'msg': 'proxy not found'}
        else:
            data = {'code': 200, 'msg': 'success', 'proxies': to_json(proxies)}
        return data


@tag_bp.route("/tag/")
def tags():
    # /tag/ 首页返回数据
    data = {
        "tag/http": " return all http protocol proxies",
        "tag/https": " return all https protocol proxies",
        "tag/http/num": " return the num of  http protocol proxies ",
        "tag/https/num": " return the num of  https protocol proxies",
    }
    return data
