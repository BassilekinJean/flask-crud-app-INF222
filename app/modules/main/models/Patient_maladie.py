from app.db.db import db

patient_maladie = db.Table(
    'patient_maladie',
    db.Column('patient_id', db.Integer, db.ForeignKey('patients.id'), primary_key=True),
    db.Column('maladie_id', db.Integer, db.ForeignKey('maladies.id'), primary_key=True)
)