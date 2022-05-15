from flask import Flask, jsonify, request

app = Flask(__name__)

global todos

todos = [ 
        { 
            "label": "My first task", "done": False 
        } 
    ]

@app.route('/todos', methods=['GET', 'POST'])
def add_new_todo():

    json_todos = jsonify(todos)
    return json_todos

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

  