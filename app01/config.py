import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False
ENV = "production"
if "LOGLEVEL" in os.environ and os.environ.get("LOGLEVEL").upper() == "DEBUG":
    DEBUG = True
if DEBUG:
    ENV = "development"

AWS_CODEGURU_PROFILER_GROUP_NAME = os.environ.get(
    "AWS_CODEGURU_PROFILER_GROUP_NAME", "test"
)
DATETELLER_BACKEND = os.environ.get("DATETELLER_BACKEND", None)
DATETELLER_BACKEND_OVERRIDE = os.environ.get("DATETELLER_BACKEND_OVERRIDE", None)
if DATETELLER_BACKEND_OVERRIDE:
    DATETELLER_BACKEND = DATETELLER_BACKEND_OVERRIDE
