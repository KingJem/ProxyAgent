import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
SQLALCHEMY_COMMIT_ON_TEARDOWN = True

DEBUG = True
HOST = '0.0.0.0'
JSON_AS_ASCII = True
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:King9503@127.0.0.1:3306/test?charset=utf8mb4'
SQLALCHEMY_TRACK_MODIFICATIONS = True

CRAWLER = {

    "enc_proxy": {
        "type": 'asyncio',
        "func": "enc",
        "trigger": 'cron',
        'second': '*/5'
    }

}

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

RANDOM_TARGET_WEB = [
    "http://baicu.com",
    "http://yun.baidu.com",
]

VALIDATOR_TIMEOUT = 10
