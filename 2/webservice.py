from flask import Flask, jsonify
from flask_restful import Resource, Api, abort
import sys
sys.path.append('1/')
from main import Convert_Age_Range
import pandas as pd

app = Flask(__name__)
api = Api(app)

def Return_Result(code):
    avg_monthly_precip = pd.read_excel("cleaned_output/cleaned_data_average_and_range.xlsx")
    result_df = avg_monthly_precip.loc[avg_monthly_precip['ISO code'] == code]
    complete_data = result_df.to_dict()
    filtered_data = {"Country Name": complete_data["Country Name"],
                     "GDP": complete_data["GDP"],
                     "Youngest Age Range": Convert_Age_Range(complete_data["Age1stCode_y"][list(complete_data["Age1stCode_y"].keys())[0]])}
    return filtered_data

class Countries(Resource):
    def get(self, code):
        try:
            countries = Return_Result(code)
            return jsonify({'countries': countries})
        except:
            abort(404, message="Resource not found")

api.add_resource(Countries, '/countries/<string:code>')

if __name__ == '__main__':
    app.run(debug=True)
