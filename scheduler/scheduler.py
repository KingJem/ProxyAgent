# import sys
# from apscheduler.schedulers.blocking import BlockingScheduler
#
#
# def runScheduler():
#     scheduler_log = LogHandler("scheduler_log")
#     scheduler = BlockingScheduler(logger=scheduler_log)
#
#     scheduler.add_job(rawProxyScheduler, 'interval', minutes=5, id="raw_proxy_check", name="raw_proxy定时采集")
#     scheduler.add_job(usefulProxyScheduler, 'interval', minutes=1, id="useful_proxy_check", name="useful_proxy定时检查")
#
#     scheduler.start()
#
#
# if __name__ == '__main__':
#     runScheduler()

###    程序的调用settings 的入口程序
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
os.environ.setdefault('ProxyAgent_SETTINGS_MODULE', 'settings')
from config import settings

import importlib
from functools import partial


#


def import_by_type(_type):
    map = {
        "asyncio": "AsyncIOScheduler",
        'gevent': "GeventScheduler",
        'tornado': 'TornadoScheduler',
        'twisted': 'TwistedScheduler'
    }
    if _type not in map:
        raise KeyError('the type of crawler is not supported yet')
    mod_nam = map.get(_type)

    mod = importlib.import_module("apscheduler.schedulers" + "." + _type)
    cls = getattr(mod, mod_nam)
    return cls


for _, v in settings.CRAWLER.items():
    _type = v.get('type')
    mod = import_by_type(_type)
