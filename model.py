from sqlalchemy import create_engine

from api.app import db
from sqlalchemy_utils import ChoiceType

import os
import sys


BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

usefulproxytag = db.Table('usefulproxyta',
                          db.Column('usefulproxy_id', db.Integer, db.ForeignKey('usefulproxy.id'), primary_key=True),
                          db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True))


class BaseModel(db.Model):
    __abstract__ = True
    id = db.column(db.Integer,)
    protocol = db.column(db.String(10))
    ip_port = db.column(db.String(30))
    ip = db.column(db.String)
    port = db.column(db.String)
    area = db.column(db.String())
    res_time = db.column(db.Integer)
    timeout_error = db.column(db.Integer)
    alive_time = db.column(db.Integer)
    last_confirm = db.column(db.DATETIME)


class RawProxy(BaseModel):
    __tablename__ = 'rawproxy'
    id = db.column(db.Integer)
    protocol = db.column(db.String(10))
    ip_port = db.column(db.String(30))
    ip = db.column(db.String)
    port = db.column(db.String)
    area = db.column(db.String())
    res_time = db.column(db.Integer)
    timeout_error = db.column(db.Integer)
    alive_time = db.column(db.Integer)
    last_confirm = db.column(db.DATETIME)


class UsefulProxy(BaseModel):
    __tablename__ = 'usefulproxy'

    type_choice = ((1, '高匿'), (2, '匿名'), (3, '透明'))
    type = db.column(ChoiceType(type_choice), db.Integer())
    tags = db.relationship('Tag', secondary=usefulproxytag, ondelete='CASCADE')


class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)


def init_db():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:root@127.0.0.1:3306/test?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    db.metadata.create_all(engine)


def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        "mysql+pymysql://root:root@127.0.0.1:3306/test?charset=utf8",
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    db.metadata.drop_all(engine)


if __name__ == '__main__':
    drop_db()
    init_db()
