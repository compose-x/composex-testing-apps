import json

import boto3
from flask import Flask

APP = Flask(__name__)
APP.config.from_object("config")

from app import views
