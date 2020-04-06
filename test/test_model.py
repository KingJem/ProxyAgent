#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from model import RawProxy

engine = create_engine("mysql+pymysql://root:root@127.0.0.1:3306/test?charset=utf8", max_overflow=0, pool_size=5)
Session = sessionmaker(bind=engine)

# 每次执行数据库操作时，都需要创建一个session
# session = Session()

session = scoped_session(Session)

# ############# 执行ORM操作 #############
obj1 = RawProxy()
# session.add(obj1)




#  查

# obj = session.query(Users).filter(Users.id > 2)
# for i in obj:
#     print(i.name)


# 改
obj = session.query(Users).filter(Users.id==2).update({"name":'tet'})
print(obj)

# 提交事务
# session.commit()
# 关闭session
session.close()