from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True)
    name = db.Column(db.String(64), index=True)
    gender = db.Column(db.Integer, index=True)
    image = db.Column(db.BLOB)

    def __repr__(self):
        return '<User {}>'.format(self.email)
