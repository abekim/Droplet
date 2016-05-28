"""
Blogger routes package

author: @abekim
"""

from blogger import app, models
from flask import render_template
from blog import *

@app.route('/')
def welcome():
    # Any notifications?
    new_post_success = 1 if request.args.get("new_post_success") else 0

    # Get all post documents in the DB
    posts = models.Post.objects()

    return render_template("index.html", title="Welcome", posts=posts, new_post_success=new_post_success)
