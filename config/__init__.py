import os
import importlib
from config import global_settings


class Settings(object):
    def __init__(self):
        for setting in dir(global_settings):
            if setting.isupper():
                k = setting
                v = getattr(global_settings, setting)
                setattr(self, k, v)
        mod = os.environ.get('global_settings')
        module = importlib.import_module(mod)

        for setting in dir(module):
            if setting.isupper():
                k = setting
                v = getattr(module, setting)
                setattr(self, k, v)


settings = Settings()
