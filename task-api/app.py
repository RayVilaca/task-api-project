from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__.split('.')[0])

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    pass

@app.route('/tasks', methods=['GET'])
def get_tasks():
    pass

@app.route('/tasks/<int:id>', methods=['PATCH'])
def update_task(id):
    data = request.get_json()
    pass

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    pass