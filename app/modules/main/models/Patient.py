from app.db.db import db
from .Personne import Personne
from .Patient_maladie import patient_maladie

class Patient(Personne, db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    prenom = db.Column(db.String(100))
    numTel = db.Column(db.Integer, unique=True)
    email = db.Column(db.String(100), unique=True)
    symptomes = db.Column(db.String(500), nullable=True)

    maladies = db.relationship(
        'Maladie',
        secondary=patient_maladie,
        back_populates='patients'
    )

    def __init__(self, nom, prenom, numTel, email, symptomes, **kwargs):
        Personne.__init__(self, nom, prenom, numTel, email)
        self.symptomes = symptomes

    def __repr__(self):
        return f'<Patient {self.id} {self.nom} {self.prenom} {self.numTel} {self.email}>'

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'prenom': self.prenom,
            'numTel': self.numTel,
            'email': self.email,
            'symptomes': self.symptomes
        }