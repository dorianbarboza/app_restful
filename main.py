from flask import Flask
from flask_restful import Api
from flask_restful import Resource

from Class.helloworld import HelloWorld

AppInstanceFlask = Flask(__name__)
ApiInstanceRestful = Api(AppInstanceFlask)

ApiInstanceRestful.add_resource(HelloWorld, '/helloworld/')


if __name__ == '__main__':
    AppInstanceFlask.run(host = '127.0.0.1', debug = True, port = 8080)
