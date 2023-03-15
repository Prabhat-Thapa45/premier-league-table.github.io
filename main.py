"""main module"""

from flask import Flask
from flask_restful import Api
from src.index import Bundesliga, Laliga, Premier


app = Flask(__name__)
api = Api(app)

api.add_resource(Premier, "/premier")
api.add_resource(Laliga, "/laliga")
api.add_resource(Bundesliga, "/bundesliga")

if __name__ == '__main__':
    app.run(debug=True)