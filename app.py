from app import Flask, request, jsonify

app = Flask(__name__)

tasks = [
    {"id": 101, "name": "Process Data"},
    {"id": 102, "name": "Send Email"},
    {"id": 103, "name": "Generate Report"}
]

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Dockerized Tasks Flask App!"})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

@app.route('/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if str(task['id']) == task_id), None)
    if task:
        return jsonify(task), 200
    else:
        return jsonify({"error": "Task not found"}), 404
    
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = request.get_json()
    tasks.append(new_task)
    return jsonify(new_task), 201


@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    app.run()