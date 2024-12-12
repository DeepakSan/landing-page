from .extensions import db

class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)