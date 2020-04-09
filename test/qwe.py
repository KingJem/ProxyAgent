l = {'trigger': 'cron', 'second': '*/20'}


def xxx(s, L):
    t = 1


xxx(2, **l)

from apscheduler.schedulers.background import BackgroundScheduler

s = BackgroundScheduler()

s.add_job()

#
# def add_job(self, func, trigger=None, args=None, kwargs=None, id=None, name=None,
#             misfire_grace_time=undefined, coalesce=undefined, max_instances=undefined,
#             next_run_time=undefined, jobstore='default', executor='default',
#             replace_existing=False, **trigger_args):
