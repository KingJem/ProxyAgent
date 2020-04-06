import os
import sys

from flask import Flask, jsonify, Response, render_template, session, request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

from api.views.tag import tags
from api.views.api import api

app = Flask(__name__)  # 创建一个Flask app对象


# 数据库链接的配置，此项必须，格式为（数据库+驱动://用户名:密码@数据库主机地址:端口/数据库名称）
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/flask_ttc'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 跟踪对象的修改，在本例中用不到调高运行效率，所以设置为False
db = SQLAlchemy(app=app)  # 为哪个Flask app对象创建SQLAlchemy对象，赋值为db
# manager = Manager(app=app)  # 初始化manager模块


# class JSONResponse(Response):
#     """
#     # 自定义flask类中的Response对象的格式
#     """
#
#     @classmethod
#     def force_type(cls, response, environ=None):
#         if isinstance(response, dict):
#             response = jsonify(response)
#             # jsonify除了将字典转换成json对象，还将把对象包装成一个Response对象
#             return super(JSONResponse, cls).force_type(response, environ)
#
#
# app.response_class = JSONResponse

#
# @app.before_request
# def process_request(*args, **kwargs):
#     if request.user_agent == "PostmanRuntime/7.21.0":
#         session['is_api'] = '0'
#     else:
#         session['is_api'] = '1'


app.route('/')
def index():
    return 'index'


app.register_blueprint(tags)
app.register_blueprint(api)



if __name__ == '__main__':
    app.run(debug=True)
