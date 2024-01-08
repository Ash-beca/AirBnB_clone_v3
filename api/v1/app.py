#!/usr/bin/python3
"""
Sets up Flask application

"""


from os import getenv
from flask import Flask, make_response, jsonify
from flask_cors import CORS

from api.v1.views import app_views
from models import storage

app = Flask(__name__)
CORS(app, orgins='0.0.0.0')
app.register_blueprint(app_views)


