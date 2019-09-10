__author__ = "Paul Schifferer <paul@schifferers.net>"

from flask import Blueprint, make_response, render_template, g
import json
import mellon_app_core
from . import blueprint

bp = blueprint.blueprint
app = mellon_app_core.create_app(blueprint_modules=[bp])
