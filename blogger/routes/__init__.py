"""
Blogger routes package

author: @abekim
"""

from blogger import app, models
from flask import render_template
from blog import *

@app.route('/')
def welcome():
    # Get all post documents in the DB
    posts = models.Post.objects()

    return render_template("index.html", title="Welcome", posts=posts)
