
from flask import Flask, jsonify
app = Flask(__name__)             # create an app instance

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route("/")                
def hello():                     
    return "Hello World!"  


@app.route('/tasks', methods=['GET'])                  
def get_tasks():
    return jsonify({'tasks': tasks}) 

                                   
if __name__ == "__main__":        # on running python app.py
    app.run()                     # run the flask app