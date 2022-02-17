"""Does all the main stuff"""

import pandas as pd
import numpy as np
import json
from flask import render_template
from flask_restful import Resource, original_flask_make_response



def serialize():
    df = pd.read_html("https://www.theguardian.com/football/premierleague/table")[0].drop("Form", axis=1)
    return np.array(df).tolist()


class Index(Resource):
    """returns table of premire leage
    """
    def get(self) -> json:
        """a dataframe is returned
        """
        headers = {'Content-Type': 'text/html'}
        return original_flask_make_response(render_template("football.html", data=serialize()), 200, headers)
        
