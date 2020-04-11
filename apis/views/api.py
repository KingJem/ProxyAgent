from flask import Blueprint

api = Blueprint('api', __name__)


# from apis.models.proxy import RawProxy


def to_json(all_vendors):
    v = [ven.to_dict() for ven in all_vendors]
    return v


@api.route('/')
def index():
    data = {'get': 'return a random ip ',
            'get_all': 'return all useful ips',
            'delete': 'delete ip '}
    return data


@api.route('/get')
def get():
    """
    return a random proxy
    返回一个随机可用的代理
    """
    pass


@api.route('/get_all')
def getall():
    return 's'


@api.route('/status')
def status():
    pass
