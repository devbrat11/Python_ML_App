
from flask import Flask, jsonify
from DataAnalyzer import TestAnalyzer
app = Flask(__name__)            


@app.route("/")                
def analysis(): 
    return "App is running..."  


@app.route('/analyze', methods=['GET'])                  
def analysis():
    testAnalyzer = TestAnalyzer()
    result = testAnalyzer.Analysis()                    
    return result   

                                   
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app