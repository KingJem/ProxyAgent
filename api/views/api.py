from flask import Blueprint, session
from flask import render_template, request

api = Blueprint('tag', __name__, url_prefix='api', template_folder='api')


@api.route('/')
def tag_relative():
    return render_template('tag.html')


@api.before_request
def process_request(*args, **kwargs):
    if request.user_agent == "PostmanRuntime/7.21.0":
        session['is_api'] = '0'
    else:
        session['is_api'] = '1'
