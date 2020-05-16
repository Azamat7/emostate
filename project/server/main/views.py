import os
import requests

from flask import render_template, Blueprint

from project.server.utils import get_nums


main_blueprint = Blueprint("main", __name__,)


@main_blueprint.route('/', methods=["GET"])
def index():
  return render_template('index.html')


@main_blueprint.route('/test', methods=['GET'])
def test():
  return render_template('test.html', nums=get_nums())
