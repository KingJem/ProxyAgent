import os
import sys

from flask import Blueprint
from flask import render_template


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)



tags = Blueprint('tags', __name__, url_prefix='/tags')


@tags.route('/')
def tag_relative():
    return render_template('tags.html')


@tags.route('/http/')
def tag_http():

    return "/tags/http"


@tags.route('/https/')
def tag_https():
    return "/tags/https"


@tags.route('/trans/')
def trans():
    return 'trans'


@tags.route('/anony/')
def anony():
    return 'anony'


@tags.route('/elite/')
def elite():
    return 'elite'


@tags.route('/trans/http')
@tags.route('/http/trans/')
def http_trans():
    return 'http/trans'


@tags.route('/anony/http')
@tags.route('/http/anony/')
def http_anony():
    return 'http/anony'


@tags.route('/elite/http/')
@tags.route('/http/elite/')
def http_elite():
    return 'http/elite'


@tags.route('/trans/https/')
@tags.route('/https/trans/')
def https_trans():
    return 'https/trans'


@tags.route('/anony/https/')
@tags.route('/https/anony/')
def https_anony():
    return 'https/anony'


@tags.route('/elite/https/')
@tags.route('/https/elite/')
def https_elite():
    return 'https/elite'
