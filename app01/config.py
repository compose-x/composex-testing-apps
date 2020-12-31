import os


_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
ENV = "production"
if "LOGLEVEL" in os.environ and os.environ.get("LOGLEVEL").upper() == "DEBUG":
    DEBUG = True
if DEBUG:
    ENV = "development"

AWS_CODEGURU_PROFILER_GROUP_NAME = "test"
if "AWS_CODEGURU_PROFILER_GROUP_NAME" in os.environ and os.environ.get("AWS_CODEGURU_PROFILER_GROUP_NAME"):
    AWS_CODEGURU_PROFILER_GROUP_NAME = os.environ.get("AWS_CODEGURU_PROFILER_GROUP_NAME")
