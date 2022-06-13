import json

import boto3
import requests
from flask import Flask, jsonify, make_response

APP = Flask(__name__)
APP.config.from_object("config")


def send_message(payload, queue_name, session=None, client=None):
    """
    Function to send a message in SQS

    :param payload: the payload to send
    :param queue_name: the name or URL of the queue
    :param session: boto3 session to override with
    :param client: boto3 client to override with
    """
    queue_url = None
    if isinstance(payload, dict):
        payload = json.dumps(payload)
    if session is None:
        session = boto3.session.Session()
    if client is None:
        client = session.client("sqs")
    if queue_name.startswith("https://"):
        queue_url = queue_name
    else:
        try:
            queue_url = client.get_queue_url(QueueName=queue_name)
        except Exception as error:
            print(error)
    if queue_url:
        client.send_message(QueueUrl=queue_url, MessageBody=payload)


@APP.route("/", methods=["GET"])
def hello():
    """
    Simple Hello World function
    """
    answer = dict()
    answer["reason"] = "Hello user"
    return make_response(jsonify(answer), 200)


@APP.route("/date")
@APP.route("/date/<date_format>")
def query_date(date_format=None):
    """
    Function to query the date service
    """
    date_app = APP.config["DATETELLER_BACKEND"]
    APP.logger.debug(f"config.DATETELLER_BACKEND => {date_app}")
    protocol = "http://"
    date_port = 5000
    path = "/date"
    if date_format:
        path = f"{path}/{date_format}"
    response = {"date": "unknown"}
    _url = f"{protocol}{date_app}:{date_port}{path}"
    APP.logger.info(f"Attempting to call {_url}")
    try:
        r_get = requests.get(_url)
        print(r_get)
        APP.logger.info(r_get)
        if 200 <= r_get.status_code < 230:
            APP.logger.info(f"CODE IS {r_get.status_code}")
            APP.logger.info(r_get.text)
            try:
                return make_response(jsonify(r_get.json), 200)
            except Exception as error:
                print(error)
                APP.logger.error(error)
                return make_response(r_get.text, 200)
    except Exception as error:
        print(error)
        APP.logger.error(error)
        return make_response(jsonify(response), 404)
