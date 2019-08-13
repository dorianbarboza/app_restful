from flask import Flask
from flask_restful import Api
from flask_restful import Resource

# Database
import psycopg2
from flask_sqlalchemy import SQLAlchemy

from Class.helloworld import HelloWorld
#from Class.Artist import Artist




AppInstanceFlask = Flask(__name__)
ApiInstanceRestful = Api(AppInstanceFlask)
AppInstanceFlask.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
AppInstanceFlask.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dorian:dorian12345@localhost/app_bd'
DatabaseInstanceAlchemy = SQLAlchemy(AppInstanceFlask)

class Person(DatabaseInstanceAlchemy.Model):
    id = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    firstName = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(120), unique = False)
    lastName = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(120), unique = False)
    email = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(120), unique = False)

    def __init__(self, firstName, lastName, email):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

ApiInstanceRestful.add_resource(HelloWorld, '/helloworld/')


if __name__ == '__main__':
    AppInstanceFlask.run(host = '127.0.0.1', debug = True, port = 8080)
    DatabaseInstanceAlchemy.create_all()
