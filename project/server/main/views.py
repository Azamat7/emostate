import os
import requests

from flask import render_template, Blueprint, redirect, request

from project.server.utils import get_nums


main_blueprint = Blueprint("main", __name__,)

signed_in = False
USERNAME = None
USERNAMES_VALID = ["azamat", "seungjun"]
PASSWORDS_VALID = dict()
PASSWORDS_VALID["azamat"] = "123"
PASSWORDS_VALID["seungjun"] = "456"


@main_blueprint.route('/', methods=["GET"])
def outdoor_activity():
  if not signed_in:
    return redirect("login")
  return render_template('outdoor_activity.html', user=(USERNAME or request.args.get('user')))


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
  global signed_in
  global USERNAME
  if request.method == 'GET':
    if signed_in:
      return redirect("/")
    return render_template("login.html", error=False)
  elif request.method == 'POST':
    print(request.form.get("username"))
    input_username = request.form.get("username")
    if input_username in USERNAMES_VALID and request.form.get("password") == PASSWORDS_VALID[input_username]:
      signed_in = True
      USERNAME = input_username
      return redirect("/")
    return render_template("login.html", error=True)


@main_blueprint.route('/app_usage', methods=['GET', 'POST'])
def app_usage():
  return render_template('app_usage.html', day = (request.args.get('day') or "8"), user=request.args.get('user'))


@main_blueprint.route('/recommendation', methods=['GET'])
def recommendation():
  return render_template('recommendation.html', user=request.args.get('user'))
