from flask import Blueprint

api = Blueprint('api', __name__, url_prefix='/api', template_folder='api')




@api.route('/')
def index():
    return


@api.route('/get')
def get():
    """
    return a random proxy
    返回一个随机可用的代理
    """
    pass


@api.route('/get_all')
def getall():
    """
    返回一个随机
    """
    pass


@api.route('/status')
def status():
    pass
