class Personne:
    def __init__(self, nom, prenom, numTel, email):
        self.nom = nom
        self.prenom = prenom
        self.numTel = numTel
        self.email = email

    def __repr__(self):
        return f'<Personne {self.nom} {self.prenom} {self.numTel} {self.email}>'
    
    def to_dict(self):
        return {
            'nom': self.nom,
            'prenom': self.prenom,
            'numTel': self.numTel,
            'email': self.email
        }