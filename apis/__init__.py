from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.debug = True
# app.config.from_object(config[config_name])
app.config.from_pyfile('../settings.py')

db = SQLAlchemy(app=app)
