"""
Routes relevant to blog objects (post, comments, etc.)

author: @abekim
"""
from blogger import app
from flask import render_template


# routes
@app.route("/")
def welcome():
    return render_template("index.html", title="Welcome", tasks=Task.objects())



@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        app.logger.info("New task, \"%s\" added", request.form['description'])
        description = request.form['description']

        t = Task(description=description)

        t.save()
    return jsonify(data=t)
