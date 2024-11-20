from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)  

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "link": self.link,
            "user_id": self.user_id
        }
