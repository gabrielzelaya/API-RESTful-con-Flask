from flask import Flask, jsonify, request
#Primero, asegúrate de tener Flask instalado.

app = Flask(__name__)

# Datos de ejemplo
todos = [
    {"id": 1, "task": "Learn Python", "completed": False},
    {"id": 2, "task": "Build a RESTful API", "completed": False},
]

@app.route('/api/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/api/todo/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if todo:
        return jsonify(todo)
    return jsonify({"message": "Todo not found"}), 404

@app.route('/api/todo', methods=['POST'])
def create_todo():
    new_todo = {
        "id": len(todos) + 1,
        "task": request.json.get("task"),
        "completed": False,
    }
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/api/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((todo for todo in todos if todo["id"] == id), None)
    if todo:
        todo["task"] = request.json.get("task", todo["task"])
        todo["completed"] = request.json.get("completed", todo["completed"])
        return jsonify(todo)
    return jsonify({"message": "Todo not found"}), 404

@app.route('/api/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [todo for todo in todos if todo["id"] != id]
    return jsonify({"message": "Todo deleted"})

if __name__ == '__main__':
    app.run(debug=True)
