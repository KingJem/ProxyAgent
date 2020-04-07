#!/usr/bin/python
# coding:utf-8

import glob
import os
import sys

try:
    import simplejson as json
except:
    import json

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    # 注册蓝本
    from api.views import module
    app.register_blueprint(module, url_prefix='/')

    module_files = glob.glob('app/views/*.py')
    fromlist = []
    for filename in module_files:
        basename = os.path.basename(filename)
        module_name = basename[0:basename.find('.')]
        if module_name == '__init__':
            continue
        fromlist.append(module_name)

    package = __import__('api.views', fromlist=fromlist)
    for module_name in fromlist:
        module = getattr(package, module_name)
        sys.stderr.write('import module: %s\n' % module_name)
        app.register_blueprint(module.module, url_prefix='/' + module_name)
    return app
