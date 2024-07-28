from src import app
from flask import render_template, flash, redirect, url_for
from src.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"user_name": "Peri"}
    posts = [
        {"author": {"user_name": "Yoru"}, "body": "Never show weakness. Ever."},
        {"author": {"user_name": "Jhin"}, "body": "The stage is set."},
    ]
    return render_template("index.html", title="Home Page", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form: LoginForm = LoginForm()
    if form.validate_on_submit():
        flash(
            f"Login requested from user [{form.username.data}], "
            f"remember_me={form.remember_me.data}"
        )
        return redirect(url_for("index"))

    return render_template("login.html", title="Sign In", form=form)
