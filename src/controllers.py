__author__ = "Paul Schifferer <paul@schifferers.net>"

# Import flask dependencies
from flask import (
    Blueprint,
    request,
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
    make_response,
)

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
# from app import db
from app.common import constants

import json


# Define the blueprint: 'auth', set its url prefix: app.url/auth
core = Blueprint("core", __name__, url_prefix="/")


# Set the route and accepted methods
@core.route("/", methods=["GET"])
def index():
    return render_template("main.html")


@core.route("status", methods=["GET"])
def status():
    try:
        r = {
            "status": "healthy",
            # 'table': constants.SLACK_GITHUB_MAP_TABLE_NAME,
            # 'users': db.scan(TableName=constants.SLACK_GITHUB_MAP_TABLE_NAME,
            #                  Select='COUNT').get('Count')
        }
    except Exception as e:
        r = {"status": "error", "error": f"{e}"}
    resp = make_response(json.dumps(r))
    resp.mimetype = "application/json"
    return resp
