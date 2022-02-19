"""Does all the main stuff"""

import pandas as pd
import numpy as np
import json
from flask import render_template
from flask_restful import Resource, original_flask_make_response



def serialize(league):
    link = {'Premier': "https://www.theguardian.com/football/premierleague/table", 
    "Laliga": "https://www.theguardian.com/football/laligafootball/table",
    "Bundesliga": "https://www.theguardian.com/football/bundesligafootball/table"
    }
    df = pd.read_html(link[league])[0].drop("Form", axis=1)
    return np.array(df).tolist()


class Premier(Resource):
    """returns table of premire leage
    """
    def get(self) -> json:
        """a dataframe is returned
        """
        headers = {'Content-Type': 'text/html'}
        return original_flask_make_response(render_template("football.html", data=serialize("Premier"), league="Premier Leage Table"), 200, headers)
        
class Laliga(Resource):
    """returns table of premire leage
    """
    def get(self) -> json:
        """a dataframe is returned
        """
        headers = {'Content-Type': 'text/html'}
        return original_flask_make_response(render_template("football.html", data=serialize('Laliga'), league="Laliga Table"), 200, headers)


class Bundesliga(Resource):
    """returns table of premire leage
    """
    def get(self) -> json:
        """a dataframe is returned
        """
        headers = {'Content-Type': 'text/html'}
        return original_flask_make_response(render_template("football.html", data=serialize('Bundesliga'), league="Bundesliga Table"), 200, headers)
