import importlib
import threading


class ThreadSafeSingleton(type):
    _instance = {}
    _singleton_lock = threading.RLock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            with cls._singleton_lock:
                if cls not in cls._instance:
                    cls._instance[cls] = super(ThreadSafeSingleton, cls).__call__(*args, **kwargs)
        return cls._instance[cls]


class SingletonScheduler(metaclass=ThreadSafeSingleton):

    def __init__(self, _type):
        self._type = _type
        map = {
            'background': 'BackgroundScheduler',
            "asyncio": "AsyncIOScheduler",
            'gevent': "GeventScheduler",
            'tornado': 'TornadoScheduler',
            'twisted': 'TwistedScheduler'
        }

        if _type not in map:
            raise KeyError('the type of crawler is not supported yet')
        self.cls_name = map.get(_type)

        self._moudle = importlib.import_module("apscheduler.schedulers" + "." + _type)
        self.cls_instance = getattr(self._moudle, self.cls_name)()
