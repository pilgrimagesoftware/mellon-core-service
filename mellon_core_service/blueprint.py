__author__ = "Paul Schifferer <paul@schifferers.net>"

from flask import Blueprint, make_response, render_template, g
import json

# Define the blueprint: 'core', set its url prefix: app.url/
blueprint = Blueprint("core", __name__, url_prefix="/")
# metrics = g["metrics"]


# Set the route and accepted methods
@blueprint.route("/", methods=["GET"])
# @metrics.counter(
#     "invocation_by_type",
#     "Number of invocations by type",
#     labels={"item_type": lambda: request.view_args["type"]},
# )
def index():
    return render_template("main.html")


@blueprint.route("/status", methods=["GET"])
# @metrics.do_not_track()
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
