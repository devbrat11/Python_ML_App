
from flask import Flask,request, jsonify
from DataAnalyzer import TestAnalyzer

app = Flask(__name__)            


@app.route("/")                
def status(): 
    return "App is running..."  


@app.route('/analyze', methods=['GET'])                  
def analysis():
    testAnalyzer = TestAnalyzer()
    result = testAnalyzer.Analysis()                    
    return result   


@app.route('/ml', methods=['POST'])                  
def predict():
    testAnalyzer = TestAnalyzer()
    request_data = request.get_json(force=True)
   
    result = testAnalyzer.predict(request_data['HeartRate'],request_data['Noise'])                    
    return jsonify(result)   


   

                                   
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app