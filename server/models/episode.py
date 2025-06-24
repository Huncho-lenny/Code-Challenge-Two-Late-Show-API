from . import db 
from sqlalchemy_serializer import SerializerMixin

class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    air_date = db.Column(db.Date, nullable=False)

    appearance_id = db.Column(db.Integer, db.ForeignKey('appearances.id'), nullable=False)

    serialize_rules = ('-appearance.episodes',)