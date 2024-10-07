from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
   {"label": "My first task", "done": False}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    todos_text = jsonify(todos)
    return todos_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    json_response = jsonify(todos)
    return json_response

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    json_response = jsonify(todos)
    return json_response



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)