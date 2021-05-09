import flask
from flask import render_template, jsonify, url_for, redirect, request, flash, session
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route("/")
@app.route("/index")
@login_required
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect("/index")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        password = User.query.filter_by(password=form.password.data).first()
        if user is None or password is None:
            flash("invalid username or password")
            return redirect("/login")
        login_user(user, remember=form.remember_me.data)
        return redirect("/index")
    return render_template("login.html", title = "Sign In", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/index")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect("/index")
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, name = form.name.data, email = form.email.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now a registered user! Thank you!')
        return redirect("/login")
    return render_template("register.html", form=form)


@app.route("/myposts")
@login_required
def posts():
    return render_template("posts.html")