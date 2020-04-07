import os
import sys

from sqlalchemy_utils import ChoiceType

from manage import db

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)


class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    protocol = db.Column(db.String(10))
    ip_port = db.Column(db.String(30), unique=True)
    ip = db.Column(db.String(40))
    port = db.Column(db.String(10))
    server_area = db.Column(db.String(20))
    res_time = db.Column(db.Integer)
    timeout_error = db.Column(db.Integer)
    alive_time = db.Column(db.DateTime)
    last_confirm = db.Column(db.DATETIME)
    type_choice = ((1, '高匿'), (2, '匿名'), (3, '透明'))
    type = db.Column(ChoiceType(type_choice), nullable=True),


class RawProxy(BaseModel):
    __tablename__ = 'rawproxys'

    def __repr__(self):
        return '<User %r>' % self.id


class UsefulProxy(BaseModel):
    __tablename__ = 'usefulproxys'

    def __repr__(self):
        return '<User %r>' % self.id
