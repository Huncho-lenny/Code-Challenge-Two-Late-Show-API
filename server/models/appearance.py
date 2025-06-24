from sqlalchemy.orm import validates 
from . import db

class Appearance(db.Model):
    __tablename__ = "appearances"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)

    def __init__(self, name, description=None):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Appearance {self.name}>"
    
    @validates('name')
    def validate_name(self, key, name):
        if not name:
            raise ValueError("Name cannot be empty.")
        if len(name) > 100:
            raise ValueError("Name must be less than 100 characters.")
        return name
    
    @validates('description')
    def validate_description(self, key, description):
        if description and len(description) > 255:
            raise ValueError("Description must be less than 255 characters.")
        return description  
    