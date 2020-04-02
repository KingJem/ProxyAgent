from flask import Flask

app = Flask(__name__,template_folder='templates',static_folder='statics',static_url_path='/static')

from .views.tag import tag

app.register_blueprint(tag)
