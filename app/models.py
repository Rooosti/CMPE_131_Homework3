from app import db
from datetime import datetime

#class Recipe for the database with an id (key), title, description, ingredients, instructions, and creation timestamp
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(1024))
    ingredients = db.Column(db.String(1024))
    instructions = db.Column(db.String(1024))
    created = db.Column(db.DateTime, default=datetime.utcnow)

#Return value of representation of the Recipe class
    def __repr__(self):
        return f'<Recipe #{self.id}: {self.title}>'
