

# 📚 Documentation API Flask

## URL de base

LE port en local est 5002 en utilisant docker

### Lien SWAGGER pour la documentation dynamique des endpoints

- **URL** `http://localhost:5000/apidocs`



---

## 1. Patients

### Lister tous les patients
- **GET** `/patients`

### Récupérer un patient par ID
- **GET** `/patients/<id>`

### Rechercher un patient par nom
- **GET** `/patients/nom/<nom>`

### Créer un patient
- **POST** `/patients`
- **Body (raw, JSON)** :
    ```json
    {
      "nom": "Doe",
      "prenom": "John",
      "numTel": 123456789,
      "email": "john.doe@email.com",
      "symptomes": "fièvre, toux"
    }
    ```

### Modifier un patient
- **PUT** `/patients/<id>`
- **Body (raw, JSON)** : (même format que POST)

### Supprimer un patient
- **DELETE** `/patients/<id>`

---

## 2. Maladies

### Lister toutes les maladies
- **GET** `/maladies`

### Récupérer une maladie par ID
- **GET** `/maladies/<id>`

### Rechercher une maladie par nom
- **GET** `/maladies/nom/<nom>`

### Créer une maladie
- **POST** `/maladies`
- **Body (raw, JSON)** :
    ```json
    {
      "nom": "Grippe",
      "description": "Infection virale",
      "type": "Virale",
      "symptomes": "fièvre, courbatures"
    }
    ```

### Modifier une maladie
- **PUT** `/maladies/<id>`
- **Body (raw, JSON)** : (même format que POST)

### Supprimer une maladie
- **DELETE** `/maladies/<id>`

---

## 3. Association Patient/Maladie

### Associer des maladies à un patient
- **POST** `/patients/<patient_id>/maladies`
- **Body (raw, JSON)** :
    ```json
    {
      "maladie_ids": [1, 2]
    }
    ```

### Lister les maladies d’un patient
- **GET** `/patients/<id>/maladies`

### Lister les patients d’une maladie
- **GET** `/maladies/<id>/patients`

---

## 4. Images

### Lister toutes les images
- **GET** `/images`

### Récupérer une image par ID (métadonnées)
- **GET** `/images/<id>`

### Télécharger une image (fichier)
- **GET** `/images/<id>/download`

### Ajouter une image
- **POST** `/images`
- **Body (form-data)** :
    - `url` : (texte, optionnel)
    - `description` : (texte)
    - `maladie_id` : (texte, id de la maladie)
    - `data` : (fichier, type File)

### Supprimer une image
- **DELETE** `/images/<id>`

---

## 5. Exemples de requêtes Postman

### Créer un patient (POST)
- Méthode : POST
- URL : `/patients`
- Body : raw, JSON (voir plus haut)

### Associer des maladies à un patient (POST)
- Méthode : POST
- URL : `/patients/1/maladies`
- Body : raw, JSON
    ```json
    {
      "maladie_ids": [2, 3]
    }
    ```

### Ajouter une image (POST)
- Méthode : POST
- URL : `/images`
- Body : form-data
    - `description` : "Radio thorax"
    - `maladie_id` : 1
    - `data` : (choisir un fichier image)

---

## Remarques

- Pour les requêtes POST/PUT avec JSON, choisis "Body" → "raw" → "JSON" dans Postman.
- Pour l’upload d’image, choisis "Body" → "form-data" et mets le champ `data` en type "File".
- Les réponses sont généralement au format JSON, sauf pour le téléchargement d’image (`/download`).

---
