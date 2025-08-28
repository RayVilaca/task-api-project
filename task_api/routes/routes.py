from flask import Blueprint, request, jsonify
from task_api.models.task import db, Task

task_bp = Blueprint("task", __name__)

@task_bp.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()

    if not data or 'title' not in data or 'done' not in data:
        return jsonify({"error": "Invalid data."}), 400
    
    new_task = Task(title=data['title'], done=data['done'])
    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@task_bp.route('/tasks/<int:id>', methods=['PATCH'])
def update_task(id):
    data = request.get_json()

    if not data or ('title' not in data and 'done' not in data):
        return jsonify({"error": "Invalid data!"}), 400
    
    task = db.get_or_404(Task, id)
    if 'title' in data:
        task.title = data['title']
    if 'done' in data:
        task.done = data['done']
    
    try:
        db.session.commit()
        return jsonify(task.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = db.get_or_404(Task, id)
    db.session.delete(task)
    db.session.commit()
    return jsonify(task.to_dict()), 200