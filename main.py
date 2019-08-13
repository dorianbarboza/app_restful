from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy

import psycopg2

from Class.helloworld import HelloWorld
#from Class.Artista import Artista

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

class Artista(DatabaseInstanceAlchemy.Model):
    ID_Artista = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    Seudonimo = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Nombre = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Apellido = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    FechaNacimiento = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Date, unique = False)
    Ciudad = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Pais = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    UrlImg = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(100), unique = False)

    def __init__(self, Seudonimo, Nombre, Apellido, FechaNacimiento, Ciudad, Pais, UrlImg):
        self.Seudonimo = Seudonimo
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.FechaNacimiento = FechaNacimiento
        self.Ciudad = Ciudad
        self.Pais = Pais
        self.UrlImg = UrlImg

class Album(DatabaseInstanceAlchemy.Model):
    ID_Album = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    NombreAlbum = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Publicacion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Date, unique = False)
    CiudadGrabacion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    PaisGrabacion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    Duracion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Time, unique = False)
    UrlImgAlbum = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(100), unique = False)
    # FK ID_Artista Artista

    def __init__(self, NombreAlbum, Publicacion, CiudadGrabacion, PaisGrabacion, Duracion, UrlImgAlbum):
        self.NombreAlbum = NombreAlbum
        self.Publicacion = Publicacion
        self.CiudadGrabacion = CiudadGrabacion
        self.PaisGrabacion = PaisGrabacion
        self.Duracion = Duracion
        self.UrlImgAlbum = UrlImgAlbum

class Cancion(DatabaseInstanceAlchemy.Model):
    ID_Cancion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Integer, primary_key = True)
    NombreCancion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(30), unique = False)
    DuracionCancion = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.Time, unique = False)
    UrlSong = DatabaseInstanceAlchemy.Column(DatabaseInstanceAlchemy.String(100), unique = False)
    # FK ID_Album Album

    def __init__(self, NombreCancion, DuracionCancion, UrlSong):
        self.NombreCancion = NombreCancion
        self.DuracionCancion = DuracionCancion
        self.UrlSong = UrlSong

ApiInstanceRestful.add_resource(HelloWorld, '/helloworld/')


if __name__ == '__main__':
    AppInstanceFlask.run(host = '127.0.0.1', debug = True, port = 8080)
    DatabaseInstanceAlchemy.create_all()
