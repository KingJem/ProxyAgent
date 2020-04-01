import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)


sys.path.append(BASE_DIR)
os.environ.setdefault('global_settings', 'settings')

from config import settings

print(settings.NAME)
print(settings.AGE)
