import os
import requests

from flask import render_template, Blueprint, request

from project.server.utils import get_nums


main_blueprint = Blueprint("main", __name__,)


@main_blueprint.route('/', methods=["GET"])
def outdoor_activity():
  return render_template('outdoor_activity.html')


@main_blueprint.route('/app_usage', methods=['GET', 'POST'])
def app_usage():
  return render_template('app_usage.html', day = (request.args.get('day') or "8"))

@main_blueprint.route('/recommendation', methods=['GET'])
def recommendation():
  return render_template('recommendation.html')
