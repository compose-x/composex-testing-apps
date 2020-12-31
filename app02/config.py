import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
ENV = "production"
if "LOGLEVEL" in os.environ and os.environ.get("LOGLEVEL").upper() == "DEBUG":
    DEBUG = True
if DEBUG:
    ENV = "development"

