
from flask import Flask,request, jsonify
from DataAnalyzer import MlAnalyser

app = Flask(__name__)            

mlAnalyzer = MlAnalyser()

@app.route("/")                
def status(): 
    return "ML App is running..."  

@app.route('/analyze', methods=['GET'])                  
def analysis():
    result = mlAnalyzer.Analysis()                    
    return result   

                                   
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app