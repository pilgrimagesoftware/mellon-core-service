__author__ = "Paul Schifferer <paul@schifferers.net>"

from flask import Blueprint, make_response, render_template, g
import json
from . import blueprint


@blueprint.route('/identity', methods=['GET'])
def get_identity():
    # TODO
    return {}


@blueprint.route('/identity', methods=['PUT'])
def put_identity():
    # TODO
    return {}
