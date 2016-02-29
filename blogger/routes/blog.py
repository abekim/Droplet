"""
Routes relevant to blog objects (post, comments, etc.)

author: @abekim
"""
from blogger import app
import datetime
from flask import render_template

@app.route("/blog/<year>/<month>/<slug>")
def get_blog(year, month, slug=""):
    # Get blog post based on date and slug
    return render_template("index.html", title="Title")
