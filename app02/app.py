#!/usr/bin/env python

import argparse
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware
from werkzeug.middleware.proxy_fix import ProxyFix
from app02 import APP


def start_app():
    debug = False
    if "DEBUG" in APP.config and APP.config["DEBUG"]:
        debug = True
        xray_recorder.configure(service=APP.name)
        XRayMiddleware(APP, xray_recorder)

    APP.wsgi_app = ProxyFix(APP.wsgi_app)
    APP.run(host="0.0.0.0", debug=debug)


if __name__ == "__main__":
    start_app()
