__author__ = "Paul Schifferer <paul@schifferers.net>"

from flask import Blueprint, make_response, render_template, g
import json
from . import blueprint


@blueprint.route("/", methods=["GET"])
# @metrics.counter(
#     "invocation_by_type",
#     "Number of invocations by type",
#     labels={"item_type": lambda: request.view_args["type"]},
# )
def index():
    return render_template("main.html")
