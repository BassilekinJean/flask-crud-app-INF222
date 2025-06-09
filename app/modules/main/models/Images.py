from app.db.db import db

class Images(db.Model):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(500), nullable=True)
    description = db.Column(db.String(500), nullable=True)
    data = db.Column(db.LargeBinary, nullable=True)
    maladie_id = db.Column(db.Integer, db.ForeignKey('maladies.id'), nullable=False)

    maladie = db.relationship('Maladie', back_populates='images')

    def __init__(self, url=None, description=None, data=None, maladie_id=None):
        self.url = url
        self.description = description
        self.data = data
        self.maladie_id = maladie_id

    def __repr__(self):
        return f"<Images id={self.id} url={self.url}>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'url': self.url,
            'description': self.description,
            'maladie_id': self.maladie_id
        }
