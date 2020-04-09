import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

validator_crawler_path = os.path.join(os.path.dirname(BASE_DIR), 'validator')

os.environ.setdefault('ProxyAgent_SETTINGS_MODULE', 'settings')
from configs import settings

from scheduler import SingletonScheduler


def validator_scheduler():
    for k, v in settings.TEST.items():
        _type = v.get('type')
        func = v.get('func')

        full_func_path = 'validator' + '.' + k + '.' + func
        print(full_func_path)

        crawler_args = v.get('crawler_args')

        test_scheduler = SingletonScheduler(_type).cls_instance

        test_scheduler.add_job(full_func_path, **crawler_args)
        return test_scheduler
