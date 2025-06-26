from flask import Flask,request,jsonify

app = Flask(__name__)
#Create a simple in-memory todo list
todo = [
    {'id': 1, 'task': 'Buy groceries'},
    {'id': 2, 'task': 'Walk the dog'},
    {'id': 3, 'task': 'Read a book'}
]
# Route and Method for adding a new todo
@app.route('/add_todo',methods=['POST'])
def add_todo():
    data = request.get_json()
    new_todo = {
        'id': len(todo) + 1,
        'task': data['task']
    } 
    todo.append(new_todo)
    return jsonify({"message": "Todo added successfully", "todo": new_todo}), 201
# Route and Method for getting all todos
@app.route('/get_todos', methods=['GET'])
def get_todos():
    return jsonify({"message": "Todos retrieved successfully", "todos": todo}), 200
# Route and Method for deleting a todo by ID
@app.route('/delete_todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todo
    for t in todo:
        if t['id'] == todo_id:
            todo.remove(t)
            break
    return jsonify({"message": "Todo deleted successfully"}), 200
# Route and Method for updating a todo by ID
@app.route('/update_todo/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    for t in todo:
        if t['id'] == todo_id:
            t['task'] = data['task']
            return jsonify({"message": "Todo updated successfully", "todo": t}), 200
    return jsonify({"message": "Todo not found"}), 404
# Route and Method for getting a todo by ID
@app.route('/get_todo/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    for t in todo:
        if t['id'] == todo_id:
            return jsonify({"message": "Todo retrieved successfully", "todo": t}), 200
    return jsonify({"message": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)