#!/usr/bin/env python

from flask import Flask
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vehicle.db'

db = SQLAlchemy(app)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_id = db.Column(db.Text)
    owner_name = db.Column(db.Text)
    vehicle_identify = db.Column(db.Text)

db.create_all()

api_manager = APIManager(app, flask_sqlalchemy_db=db)
api_manager.create_api(Vehicle, methods=['GET', 'POST', 'DELETE', 'PUT'])


if __name__=='__main__':
    app.run(debug=True)
