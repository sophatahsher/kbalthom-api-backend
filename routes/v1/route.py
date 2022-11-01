from flask import jsonify, json
from app import app
from datetime import date

config = dict(app.config)

from apps.v1.controllers.auth.user_controller import UserController

# Create Prefix API version
PREFIX="/api/v1.0"


@app.route(PREFIX +'/')
def hello():
    return 'Welcome to API section!'

@app.route(PREFIX +'/user/login')
def login():
    print('Route============')
    return UserController().login()


@app.route(PREFIX + '/not_found')
def not_found():
    return jsonify(message='The resource was not found'), 404