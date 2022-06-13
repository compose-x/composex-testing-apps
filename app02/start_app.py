#!/usr/bin/env python

from app import APP
from aws_xray_sdk.core import patch_all, xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from codeguru_profiler_agent import Profiler
from compose_x_common.compose_x_common import keyisset
from werkzeug.middleware.proxy_fix import ProxyFix


def start_app():
    debug = False
    try:
        Profiler(
            profiling_group_name=APP.config["AWS_CODEGURU_PROFILER_GROUP_NAME"]
        ).start()
    except Exception as error:
        print("FAILED TO START CODEGURU PROFILES", error)
    if keyisset("DEBUG", APP.config):
        debug = True
        xray_recorder.configure(service=APP.name)
        XRayMiddleware(APP, xray_recorder)
        xray_recorder.configure(service="app01")
        patch_all()

    APP.wsgi_app = ProxyFix(APP.wsgi_app)
    APP.run(host="0.0.0.0", debug=debug)


if __name__ == "__main__":
    start_app()
