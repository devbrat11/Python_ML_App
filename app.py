
from flask import Flask, jsonify
from DataAnalyzer import TestAnalyzer
import pandas as pd
app = Flask(__name__)            


@app.route("/")                
def status(): 
    return "App is running..."  

@app.route('/test')
def getData():
    data=pd.read_csv("HearCareHealthData.csv")
    x = data.to_json()
    return x


@app.route('/analyze', methods=['GET'])                  
def analysis():
    testAnalyzer = TestAnalyzer()
    result = testAnalyzer.Analysis()                    
    return result   

                                   
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app