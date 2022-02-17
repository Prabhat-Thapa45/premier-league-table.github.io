"""main module"""

import imp
from flask import Flask
from flask_restful import Api
from src.index import Index


app = Flask(__name__)
api = Api(app)



api.add_resource(Index, "/")

if __name__ == '__main__':
    app.run(debug=True)