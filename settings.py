DATABASE = {

}

CRAWLER = {

    "enc_proxy": {
        "type": 'asyncio',
        "func": "enc",
        "trigger": 'cron',
        'second': '*/5'
    }

}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoblog',
        'USER': 'root',
        'PASSWORD': 'King9503',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
    }
}

NAME = "KING"

SCHEDULER_ARGS = {
    'apscheduler.jobstores.mongo': {
        'type': 'mongodb'
    },
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///jobs.sqlite'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'UTC',
}

TEST = {
    # 'async_http_validator': {"type": 'asyncio', 'func': 'enc', 'crawler_args': {"trigger": 'cron', 'second': '*/20'}},
    'ttttt': {'type': 'background', 'func': 'ttt', 'crawler_args': {"trigger": 'cron', 'second': '*/2'}}

}

# 文件名字是必须的
# 函数名字是必须的
# 参数是必须的
