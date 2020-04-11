import os
import sys

from flask import Blueprint

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)

from apis.models import RawProxy

tag_bp = Blueprint('tag', __name__)


# 定义的一个将object_array 转化成json对象的方法
def to_json(all_vendors):
    v = [ven.to_dict() for ven in all_vendors]
    return v


@tag_bp.route("/tag/<protocol>/")
@tag_bp.route("/tag/<protocol>/<_type>")
def muti_tags(protocol, _type=None):
    if _type:
        ips = RawProxy.query.filter(RawProxy.protocol == protocol).all()
        data = {'code': 200, 'msg': 'success', 'ips': to_json(ips)}
        return data
    if not _type:
        ips = RawProxy.query.filter(RawProxy.protocol == protocol, RawProxy.type == _type).all()
        data = {'code': 200, 'msg': 'success', 'ips': to_json(ips)}
        return data


@tag_bp.route("/tag/")
def tags():
    data = {
        "tag/http": " return all http protocol IP record",
        "tag/https": " return all https protocol IP record",
        "tag/http/num": " return the num of  http protocol IP record",
        "tag/https/num": " return the num of  https protocol IP record",
    }
    return data
