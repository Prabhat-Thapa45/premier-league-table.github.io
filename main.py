"""main module"""

import imp
from flask import Flask
from flask_restful import Api
from src.index import Bundesliga, Laliga, Premier


app = Flask(__name__)
api = Api(app)



api.add_resource(Premier, "/premier-league-table")
api.add_resource(Laliga, "/laliga-table")
api.add_resource(Bundesliga, "/bundesliga-table")

if __name__ == '__main__':
    app.run(debug=True)