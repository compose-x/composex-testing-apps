""" MAIN VIEWS FOR FLASK APP"""

from datetime import datetime as dt

from flask import jsonify, make_response

from . import APP


@APP.route("/", methods=["GET"])
def hello():
    """
    Simple Hello World function
    """
    answer = dict()
    answer["reason"] = "This is app02"
    return make_response(jsonify(answer), 200)


@APP.route("/date", methods=["GET"])
@APP.route("/date/<utc>", methods=["GET"])
def date(utc=None):
    """
    Simple Hello World function
    """
    answer = dict()
    if utc:
        answer["date"] = dt.utcnow().isoformat()
    else:
        answer["date"] = dt.now().isoformat()
    return make_response(jsonify(answer), 200)
