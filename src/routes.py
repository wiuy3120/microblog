from src import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"user_name": "Peri"}
    posts = [
        {"author": {"user_name": "Yoru"}, "body": "Never show weakness. Ever."},
        {"author": {"user_name": "Jhin"}, "body": "The stage is set."},
    ]
    return render_template("index.html", title="Home Page", user=user, posts=posts)
