#!/usr/bin/env python

from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)

class Greeting(restful.Resource):
    def get(self):
        return {'greeting': 'Hello World'}

api.add_resource(Greeting, '/')

if __name__=='__main__':
    app.run(debug=True)

