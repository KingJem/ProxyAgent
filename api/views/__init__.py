import os

from flask import Blueprint

try:
    import simplejson as json
except:
    import json

module_file = os.path.basename(__file__)
module_name = module_file[0:module_file.find('.')]
module = Blueprint(module_name, __name__)
