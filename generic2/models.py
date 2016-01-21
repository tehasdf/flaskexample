from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Thing(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }