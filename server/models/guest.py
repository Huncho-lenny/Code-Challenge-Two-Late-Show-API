from . import db 
from sqlalchemy_serializer import SerializerMixin

class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<Guest {self.name} ({self.email})>"
    
    appearances = db.relationship('Appearance', backref='guest', cascade='all, delete-orphan')

    serialize_rules = ('-appearances.guest',)