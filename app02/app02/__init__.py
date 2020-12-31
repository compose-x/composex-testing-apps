
import boto3
import json
from flask import Flask

APP = Flask(__name__)
APP.config.from_object("config")

from app02 import views
