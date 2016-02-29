"""
Blogger routes package

author: @abekim
"""

from blogger import app
from flask import render_template
from blog import *

@app.route('/')
def welcome():
    return render_template("index.html", title="Welcome")