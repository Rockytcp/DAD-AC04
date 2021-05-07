from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from app import db
import flask

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    comment = db.Column(db.String(120))
    username = db.Column(db.String(20))
    email = db.Column(db.String(30))
    
