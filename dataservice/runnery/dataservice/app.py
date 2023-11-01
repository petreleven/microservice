from Raven.Raven import create_jsonApp
import os
from views import blueprints
import configparser
from flask_cors import CORS
from flask import request, Request, abort, globals
import jwt

_HERE = os.path.dirname(__file__)
_SETTINGS = os.path.join(_HERE, 'settings.ini')
print(_HERE)


def create_app(settings=None):
    if settings is None:
        settings = _SETTINGS

    app = create_jsonApp(isJSon=True, blueprints=blueprints)

    conf = configparser.ConfigParser()
    conf.read(_SETTINGS)
    for key in conf['flask']:
        app.config[key.upper()] = conf['flask'][key]
      
        
    with open(app.config['PUB_KEY']) as f:
        app.config['PUB_KEY'] = f.read()

    CORS(app=app)

    @app.before_request
    def before_req():
        if int(app.config.get('NEED_TOKEN')):
            authenticate(app, request)
    return app


def authenticate(app, request: Request):
    key = request.headers.get("Authorization")
    if key is None:
        return abort(401)

    key = key.split(" ")
    if len(key) != 2:
        return abort(401)

    if key[0].lower() != 'bearer':
        return abort(401)

    PUB_KEY = app.config['PUB_KEY']

    try:
        token = key[1]
        token = jwt.decode(token, PUB_KEY, algorithms=['RS512'], audience="dataservice.runnery.com")
    except Exception as e:
        return abort(401)

    globals.jwt_token = token


