"""
Blogger application

author: @abekim

Initialize an instance of a blogger app and serve it up
"""

from flask import Flask, jsonify, request
from flask.ext.cache import Cache
from flask.ext.mongoengine import MongoEngine
from config import configure

# Initialize app
app = Flask(__name__, instance_relative_config=True)
configure(app)

app.json_encoder = app.config["JSON_ENCODER"]

if not app.debug:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.DEBUG)

with app.app_context():
    cache = Cache(app)
    # Initialize db
    db = MongoEngine(app)

# Import routes
from blogger.routes import *
