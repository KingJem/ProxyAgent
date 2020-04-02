from flask import Blueprint
from flask import render_template

tag = Blueprint('tag', __name__, url_prefix='tag', template_folder='tag')


@tag.route('/')
def tag_relative():
    return render_template('tag.html')
