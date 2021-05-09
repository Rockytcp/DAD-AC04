from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app import db
import flask
from flask_login import UserMixin
from app import login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))
    name = db.Column(db.String(20))
    email = db.Column(db.String(30))
    
@login.user_loader
def load_user(id):
    return User.query.get(int(id))