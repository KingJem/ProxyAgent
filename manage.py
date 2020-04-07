# import os
#
# import click
# import sys
# import platform
#
#
# BASE_DIR = os.path.dirname(__file__)
# sys.path.append(BASE_DIR)
#
# CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
#
#
# @click.group(context_settings=CONTEXT_SETTINGS)
# def cli():
#     """ProxyPool cli工具"""
#     pass
#
#
# @cli.command(name='schedule')
# def schedule():
#     click.echo('schedule')
#
#
# @cli.command(name='api')
# def api():
#     click.echo('api')
#     if platform.system() == 'Windows':
#         click.echo('run on windows')
#     else:
#         # runFlaskWithGunicorn()
#         click.echo('other')


import os

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from api import create_app

# from api.models.proxy import RawProxy, UsefulProxy

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()

#
# if __name__ == '__main__':
#     os.environ.setdefault("ProxyAgent_SETTINGS_MODULE", "settings")
#     from configs import settings
#
#     print(settings.NAME)
#
#     # cli()
