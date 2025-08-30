from marshmallow import ValidationError
from task_api.models.task import db, Task
from flask import Blueprint, request, jsonify

from task_api.schemas.task_schema import TaskCreateSchema, TaskUpdateSchema

task_bp = Blueprint("task", __name__)


@task_bp.route("/tasks", methods=["POST"])
def create_task():
    try:
        data = TaskCreateSchema().load(request.get_json())
    except ValidationError as err:
        return {"errors": err.messages}, 400

    new_task = Task(**data)
    db.session.add(new_task)

    try:
        db.session.commit()
        return jsonify(new_task.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@task_bp.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


@task_bp.route("/tasks/<int:id>", methods=["PATCH"])
def update_task(id):
    try:
        data = TaskUpdateSchema().load(request.get_json())
    except ValidationError as err:
        return {"errors": err.messages}, 400

    task = db.get_or_404(Task, id)
    if "title" in data:
        task.set_title(data["title"])
    if "done" in data:
        task.set_done(data["done"])

    try:
        db.session.commit()
        return jsonify(task.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


@task_bp.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = db.get_or_404(Task, id)
    db.session.delete(task)

    try:
        db.session.commit()
        return jsonify(task.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
