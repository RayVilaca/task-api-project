from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def set_title(self, title):
        self.title = title

    def set_done(self, done):
        self.done = done

    def to_dict(self):
        return {"id": self.id, "title": self.title, "done": self.done}
