from scheduler import SingletonScheduler
import os
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

os.environ.setdefault('ProxyAgent_SETTINGS_MODULE', 'settings')
from config import settings



for k,v in settings.CRAWLER.items():
    print(v)


