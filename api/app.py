from flask import Flask, jsonify, Response, render_template

app = Flask(__name__)


class JSONResponse(Response):
    """
    # 自定义flask类中的Response对象的格式
    """

    @classmethod
    def force_type(cls, response, environ=None):
        if isinstance(response, dict):
            response = jsonify(response)
            # jsonify除了将字典转换成json对象，还将把对象包装成一个Response对象
            return super(JSONResponse, cls).force_type(response, environ)


app.response_class = JSONResponse


@app.route('/')
def index():
    return


@app.route('/get')
def get():
    """
    return a random proxy
    返回一个随机可用的代理
    """
    pass


@app.route('/get_all')
def getall():
    """
    返回一个随机
    """
    pass


@app.route('/status')
def status():
    pass


if __name__ == '__main__':
    app.run()
