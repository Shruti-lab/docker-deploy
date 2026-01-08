from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 101, "name": "Process Data"},
    {"id": 102, "name": "Send Email"},
    {"id": 103, "name": "Generate Report"}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Dockerized Tasks Flask App!"})

# Get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Get task by ID
@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if str(task['id']) == task_id), None)
    if task:
        return jsonify(task), 200
    else:
        return jsonify({"error": "Task not found"}), 404

# Create new task  
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    if not new_task or 'id' not in new_task or 'name' not in new_task:
        return jsonify({"error": "Invalid task data"}), 400
    tasks.append(new_task)
    return jsonify(new_task), 201


# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)