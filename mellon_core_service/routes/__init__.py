__author__ = "Paul Schifferer <paul@schifferers.net>"

from flask import Blueprint, make_response, render_template, g
import json

# Define the blueprint: 'core', set its url prefix: app.url/
blueprint = Blueprint("core", __name__, url_prefix="/")
# metrics = g["metrics"]
