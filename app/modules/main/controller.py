from flask import jsonify, request
from app.modules.main.models.Maladies import Maladie
from app.modules.main.models.Patient import Patient
from app.modules.main.models.Images import Images
from app.db.db import db


class MainController:
    def index(self):
        return {'message':'Hello, World!'}
    
    def getPatients(self):
        patients = Patient.query.all()
        return [patient.to_dict() for patient in patients]

    def getMaladies(self):
        
        maladies = Maladie.query.all()
        return [maladie.to_dict() for maladie in maladies]
    
    def getPatientById(self, id):
        patient = Patient.query.get(id)
        if patient:
            return patient.to_dict()
        else:
            return {'message': 'Patient not found'}, 404

    def getPatientByNom(self, nom):
        patients = Patient.query.filter_by(nom=nom).all()
        if patients:
            return [patient.to_dict() for patient in patients]
        else:
            return {'message': 'Patient not found'}, 404
        
    def getMaladieById(self, id):
        maladie = Maladie.query.get(id)
        if maladie:
            return maladie.to_dict()
        else:
            return {'message': 'Maladie not found'}, 404
        
    def getMaladieByNom(self, nom):
        maladies = Maladie.query.filter_by(nom=nom).all()
        if maladies:
            return [maladie.to_dict() for maladie in maladies]
        else:
            return {'message': 'Maladie not found'}, 404
        
    def addPatient(self, data):
        # If data is a list, create multiple patients
        if isinstance(data, list):
            patients = [Patient(**item) for item in data]
            db.session.add_all(patients)
            db.session.commit()
            return [patient.to_dict() for patient in patients], 201
        # Otherwise, create a single patient
        patient = Patient(**data)
        db.session.add(patient)
        db.session.commit()
        return patient.to_dict(), 201
    
    def addMaladie(self, data):
        if isinstance(data, list):
            maladies = [Maladie(**item) for item in data]
            db.session.add_all(maladies)
            db.session.commit()
            return [maladie.to_dict() for maladie in maladies], 201
        # Otherwise, create a single maladie
        maladie = Maladie(**data)
        db.session.add(maladie)
        db.session.commit()
        return maladie.to_dict(), 201

    def updatePatient(self, id, data):
        patient = Patient.query.get(id)
        if not patient:
            return {'message': 'Patient not found'}, 404
        
        for key, value in data.items():
            setattr(patient, key, value)
        
        db.session.commit()
        return patient.to_dict()
    
    def updateMaladie(self, id, data):
        
        maladie = Maladie.query.get(id)
        if not maladie:
            return {'message': 'Maladie not found'}, 404
        
        for key, value in data.items():
            setattr(maladie, key, value)
        
        db.session.commit()
        return maladie.to_dict()
    
    def deletePatient(self, id):
        patient = Patient.query.get(id)
        if not patient:
            return {'message': 'Patient not found'}, 404
        
        db.session.delete(patient)
        db.session.commit()
        return {'message': 'Patient deleted successfully'}, 204
    
    def deleteMaladie(self, id):
        
        maladie = Maladie.query.get(id)
        if not maladie:
            return {'message': 'Maladie not found'}, 404
        
        db.session.delete(maladie)
        db.session.commit()
        return {'message': 'Maladie deleted successfully'}, 204
    
    def patientMaladies(self, id):
        
        patient = Patient.query.get(id)
        if not patient:
            return {'message': 'Patient not found'}, 404
        
        # Assuming a many-to-many relationship between patients and maladies
        maladies = patient.maladies if hasattr(patient, 'maladies') else []
        return [maladie.to_dict() for maladie in maladies]
    
    def maladiePatients(self, id):
        
        maladie = Maladie.query.get(id)
        if not maladie:
            return {'message': 'Maladie not found'}, 404
        
        # Assuming a many-to-many relationship between maladies and patients
        patients = maladie.patients if hasattr(maladie, 'patients') else []
        return [patient.to_dict() for patient in patients]
    
    def getImages(self):
        images = Images.query.all()
        return [image.to_dict() for image in images]

    def addImage(self, url, description, data, maladie_id):
        image = Images(url=url, description=description, data=data, maladie_id=maladie_id)
        db.session.add(image)
        db.session.commit()
        return {"image_id": image.id}, 201
    
    def getImageById(self, id):
        image = Images.query.get(id)
        if image:
            return image.to_dict()
        else:
            return {'message': 'Image not found'}, 404
        
    def deleteImage(self, id):
        image = Images.query.get(id)
        if not image:
            return {'message': 'Image not found'}, 404
        
        db.session.delete(image)
        db.session.commit()
        return {'message': 'Image deleted successfully'}, 204
    
    def getImagesMaladies(self, id):
        
        maladie = Maladie.query.get(id)
        if not maladie:
            return {'message': 'Maladie not found'}, 404
        
        # Assuming a many-to-many relationship between maladies and images
        images = maladie.images if hasattr(maladie, 'images') else []
        return [image.to_dict() for image in images]
    
    def addMaladieToPatient(self, patient_id, maladie_ids):
        patient = Patient.query.get(patient_id)
        if not patient:
            return {"error": "Patient non trouvé"}, 404
        for maladie_id in maladie_ids:
            maladie = Maladie.query.get(maladie_id)
            if maladie and maladie not in patient.maladies:
                patient.maladies.append(maladie)
        db.session.commit()
        return patient.to_dict()
