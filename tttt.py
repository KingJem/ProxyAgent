import importlib
import os
import sys
import threading

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

os.environ.setdefault('ProxyAgent_SETTINGS_MODULE', 'settings')
from config import settings

print(settings.NAME)

# def import_by_type(_type):
#     map = {
#         "asyncio": "AsyncIOScheduler",
#         'gevent': "GeventScheduler",
#         'tornado': 'TornadoScheduler',
#         'twisted': 'TwistedScheduler'
#     }
#     if _type not in map:
#         raise KeyError('the type of crawler is not supported yet')
#     s = map.get(_type)
#
#
#     mod = importlib.import_module("apscheduler.schedulers.asyncio" )
#     return mod
#
#
# mod = import_by_type('gevent')
# print(dir(mod))

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
os.environ.setdefault('ProxyAgent_SETTINGS_MODULE', 'settings')
from config import settings

import importlib





