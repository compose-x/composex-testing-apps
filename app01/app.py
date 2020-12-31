#!/usr/bin/env python

from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from aws_xray_sdk.core import patcher, xray_recorder
from werkzeug.middleware.proxy_fix import ProxyFix
from codeguru_profiler_agent import Profiler
from app01 import APP


def start_app():
    debug = False
    Profiler(profiling_group_name=APP.config["AWS_CODEGURU_PROFILER_GROUP_NAME"]).start()
    if "DEBUG" in APP.config and APP.config["DEBUG"]:
        debug = True
        xray_recorder.configure(service=APP.name)
        XRayMiddleware(APP, xray_recorder)
        xray_recorder.configure(service="app01")

    APP.wsgi_app = ProxyFix(APP.wsgi_app)
    APP.run(host="0.0.0.0", debug=debug)


if __name__ == "__main__":
    start_app()
