import flask
from flask import render_template, jsonify, url_for, redirect, request, flash, session
from app import app, db
from app.models import User

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")