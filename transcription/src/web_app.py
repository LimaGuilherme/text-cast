# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api


web_app = None
api = None


def get_web_app() -> Flask:
    global web_app

    if not web_app:
        web_app = Flask(__name__)

    return web_app


def get_api() -> Api:
    global api

    if not api:
        api = Api(get_web_app())
    return api
