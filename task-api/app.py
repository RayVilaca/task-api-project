from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__.split('.')[0])

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/task-database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def to_dict(self):
        return {"id": self.id, 'title': self.title, 'done': self.done}

@app.route('/tasks', methods=['POST'])
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

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200

@app.route('/tasks/<int:id>', methods=['PATCH'])
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

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = db.get_or_404(Task, id)
    db.session.delete(task)
    db.session.commit()
    return jsonify(f"Task {id} deleted successfully"), 200

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)