import sys
from apscheduler.schedulers.blocking import BlockingScheduler


def runScheduler():
    scheduler_log = LogHandler("scheduler_log")
    scheduler = BlockingScheduler(logger=scheduler_log)

    scheduler.add_job(rawProxyScheduler, 'interval', minutes=5, id="raw_proxy_check", name="raw_proxy定时采集")
    scheduler.add_job(usefulProxyScheduler, 'interval', minutes=1, id="useful_proxy_check", name="useful_proxy定时检查")

    scheduler.start()


if __name__ == '__main__':
    runScheduler()
