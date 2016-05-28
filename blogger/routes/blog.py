"""
Routes relevant to blog objects (post, comments, etc.)

author: @abekim
"""
from blogger import app, models
import datetime
from flask import jsonify, render_template, request
from . import errors

# Remove later
import random

@app.route("/blog/<year>/<month>/<slug>")
def get_blog(year, month, slug=""):
    # Get blog post based on date and slug
    return render_template("index.html", title="Title")

@app.route("/blog/new", methods=['GET', 'POST'])
def post_blog():
    if request.method == 'GET':
        return render_template("newpost.html", title="Add a new blog post")
    else:
        # Get post data from payload - wherever the payload lives
        post = request.get_json()
        if post is None:
            post = request.data
        if not post:
            post = request.form
        if not post:
            return errors.internal_server_error("Unable to retrieve necessary data for post.")

        app.logger.info(post)

        author = post["author"]
        body = post["body"]
        subject = post["subject"]

        app.logger.info(author)

        # Remove later
        post_randnum = random.randint(1, 1000000)
        if (body is None):
            body = "Body " + post_randnum
        if (subject is None):
            subject = "Subject " + post_randnum
        if (author is None):
            author = "foo"

        post = models.Post(
            author=author,
            body=body,
            subject=subject
        )

        post.save()
        data = post

        return jsonify({"response":1})