from app.db.db import db
from .Patient_maladie import patient_maladie

class Maladie(db.Model):
    __tablename__ = 'maladies'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    type = db.Column(db.String(50), nullable=True)
    symptomes = db.Column(db.String(500), nullable=True)

    images = db.relationship('Images', back_populates='maladie', cascade='all, delete-orphan')

    patients = db.relationship(
        'Patient',
        secondary=patient_maladie,
        back_populates='maladies'
    )

    def __init__(self, nom, description=None, type=None, symptomes=None):
        self.nom = nom
        self.description = description
        self.type = type
        self.symptomes = symptomes

    def __repr__(self):
        return f'<Maladie {self.id} {self.nom}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'description': self.description,
            'type': self.type,
            'symptomes': self.symptomes
        }