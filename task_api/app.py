from flask import Flask
from task_api.models.task import db
from task_api.routes.routes import task_bp

def create_app(testing:bool=False):
    app = Flask(__name__.split('.')[0])

    if testing:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/task-database'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(task_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)