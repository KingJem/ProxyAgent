import os
import sys

from apis import db

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)


class BaseModel(db.Model):
    type_choice = ((1, '高匿'), (2, '匿名'), (3, '透明'))
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    protocol = db.Column(db.String(10))
    ip_port = db.Column(db.String(30), unique=True)
    server_area = db.Column(db.String(80))
    res_time = db.Column(db.Integer)
    timeout_error = db.Column(db.Integer)
    alive_time = db.Column(db.DateTime)
    last_confirm = db.Column(db.DateTime)
    num_type = db.Column(db.SMALLINT)
    type = db.Column(db.String(10))
    created_date = db.Column(db.DateTime, default=db.func.now())

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class RawProxy(BaseModel):
    __tablename__ = 'rawproxys'

    def __repr__(self):
        return '<User %r>' % self.id


class UsefulProxy(BaseModel):
    __tablename__ = 'usefulproxys'

    def __repr__(self):
        return '<User %r>' % self.id
