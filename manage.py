import os
import platform
import sys

BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from apis import app, db
from apis.views.tag import tag_bp
from apis.views.api import api

app.register_blueprint(tag_bp)
app.register_blueprint(api)

# from apis.models import RawProxy, UsefulProxy

manager = Manager(app)
migrate = Migrate(app, db)


@manager.command
def runapi():
    print('api server is starting ')
    if platform.system() == 'Windows':
        print('run on windows')
    else:
        # runFlaskWithGunicorn()
        pass


@manager.command
def schedule():
    print('schedule is starting')


@manager.command
def runcralwer():
    print('crawlers is starting')


manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    os.environ.setdefault("ProxyAgent_SETTINGS_MODULE", "settings")
    manager.run()

#
# if __name__ == '__main__':
#     os.environ.setdefault("ProxyAgent_SETTINGS_MODULE", "settings")
#     from configs import settings
#
#     print(settings.NAME)
#
#     # cli()
