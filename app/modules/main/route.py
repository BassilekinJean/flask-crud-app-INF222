from flask import Blueprint, jsonify, request, send_file, make_response
from .controller import MainController
import io

main_bp = Blueprint('main', __name__)
controller = MainController()

@main_bp.route('/')
def index():
    """
    Accueil de l'API.
    ---
    responses:
      200:
        description: Message de bienvenue
    """
    return jsonify(controller.index())

@main_bp.route('/patients', methods=['GET'])
def patients():
    """
    Liste tous les patients.
    ---
    responses:
      200:
        description: Liste des patients
    """
    return jsonify(controller.getPatients())

@main_bp.route('/patients/nom/<string:nom>', methods=['GET'])
def patient_by_nom(nom):
    """
    Recherche un ou plusieurs patients par nom.
    ---
    parameters:
      - name: nom
        in: path
        type: string
        required: true
    responses:
      200:
        description: Liste des patients trouvés
    """
    return jsonify(controller.getPatientByNom(nom))

@main_bp.route('/maladies', methods=['GET'])
def maladies():
    """
    Liste toutes les maladies.
    ---
    responses:
      200:
        description: Liste des maladies
    """
    return jsonify(controller.getMaladies())

@main_bp.route('/maladies/nom/<string:nom>', methods=['GET'])
def maladie_by_nom(nom):
    """
    Recherche une ou plusieurs maladies par nom.
    ---
    parameters:
      - name: nom
        in: path
        type: string
        required: true
    responses:
      200:
        description: Liste des maladies trouvées
    """
    return jsonify(controller.getMaladieByNom(nom))

@main_bp.route('/patients/<int:id>', methods=['GET'])
def patient_by_id(id):
    """
    Récupère un patient par son ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Patient trouvé
    """
    return jsonify(controller.getPatientById(id))

@main_bp.route('/maladies/<int:id>', methods=['GET'])
def maladie_by_id(id):
    """
    Récupère une maladie par son ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Maladie trouvée
    """
    return jsonify(controller.getMaladieById(id))

@main_bp.route('/patients', methods=['POST'])
def add_patient():
    """
    Ajoute un nouveau patient.
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            nom:
              type: string
            prenom:
              type: string
            numTel:
              type: integer
            email:
              type: string
            symptomes:
              type: string
    responses:
      201:
        description: Patient créé
    """
    data = request.get_json()
    return jsonify(controller.addPatient(data))

@main_bp.route('/maladies', methods=['POST'])
def add_maladie():
    """
    Ajoute une nouvelle maladie.
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        schema:
          type: object
          properties:
            nom:
              type: string
            description:
              type: string
            type:
              type: string
            symptomes:
              type: string
    responses:
      201:
        description: Maladie créée
    """
    data = request.get_json()
    return jsonify(controller.addMaladie(data))   

@main_bp.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    """
    Met à jour un patient existant.
    ---
    consumes:
      - application/json
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
    responses:
      200:
        description: Patient mis à jour
    """
    data = request.get_json()
    return jsonify(controller.updatePatient(id, data))

@main_bp.route('/maladies/<int:id>', methods=['PUT'])
def update_maladie(id):
    """
    Met à jour une maladie existante.
    ---
    consumes:
      - application/json
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
    responses:
      200:
        description: Maladie mise à jour
    """
    data = request.get_json()
    return jsonify(controller.updateMaladie(id, data))  

@main_bp.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    """
    Supprime un patient par son ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Patient supprimé
    """
    return jsonify(controller.deletePatient(id))  

@main_bp.route('/maladies/<int:id>', methods=['DELETE'])
def delete_maladie(id):
    """
    Supprime une maladie par son ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Maladie supprimée
    """
    return jsonify(controller.deleteMaladie(id))

@main_bp.route('/patients/<int:id>/maladies', methods=['GET'])
def patient_maladies(id):
    """
    Liste les maladies d'un patient.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Liste des maladies du patient
    """
    return jsonify(controller.patientMaladies(id))

@main_bp.route('/maladies/<int:id>/patients', methods=['GET'])
def maladie_patients(id):
    """
    Liste les patients atteints d'une maladie.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Liste des patients atteints
    """
    return jsonify(controller.maladiePatients(id))

@main_bp.route('/images', methods=['GET'])
def get_images():
    """
    Liste toutes les images.
    ---
    responses:
      200:
        description: Liste des images
    """
    return jsonify(controller.getImages())

@main_bp.route('/images/<int:id>', methods=['GET'])
def get_image(id):
    """
    Récupère une image par son ID (métadonnées).
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Image trouvée
    """
    return jsonify(controller.getImageById(id))

@main_bp.route('/images', methods=['POST'])
def add_image():
    """
    Ajoute une image à une maladie.
    ---
    consumes:
      - multipart/form-data
    parameters:
      - in: formData
        name: url
        type: string
        required: false
      - in: formData
        name: description
        type: string
        required: false
      - in: formData
        name: maladie_id
        type: integer
        required: true
      - in: formData
        name: data
        type: file
        required: false
    responses:
      201:
        description: Image ajoutée
    """
    file = request.files.get('data')
    url = request.form.get('url')
    description = request.form.get('description')
    maladie_id = request.form.get('maladie_id')
    data = file.read() if file else None

    return jsonify(controller.addImage(url, description, data, maladie_id))

@main_bp.route('/images/<int:id>/download', methods=['GET'])
def download_image(id):
    """
    Télécharge le fichier image binaire.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Fichier image téléchargé
    """
    from .models.Images import Images
    image = Images.query.get(id)
    if not image or not image.data:
        return {'message': 'Image not found'}, 404
    return send_file(
        io.BytesIO(image.data),
        mimetype='image/jpeg',  # adapte selon le type réel
        as_attachment=True,
        download_name=f'image_{id}.jpg'
    )

@main_bp.route('/images/<int:id>', methods=['DELETE'])
def delete_image(id):
    """
    Supprime une image par son ID.
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      204:
        description: Image supprimée
    """
    if not id:
        return jsonify({'message': 'Image ID is required'}), 400
    return jsonify(controller.deleteImage(id))

@main_bp.route('/patients/<int:patient_id>/maladies', methods=['POST'])
def add_maladies_to_patient(patient_id):
    """
    Associe une ou plusieurs maladies à un patient.
    ---
    consumes:
      - application/json
    parameters:
      - name: patient_id
        in: path
        type: integer
        required: true
      - in: body
        name: body
        schema:
          type: object
          properties:
            maladie_ids:
              type: array
              items:
                type: integer
    responses:
      200:
        description: Maladies associées au patient
    """
    data = request.get_json()
    maladie_ids = data.get('maladie_ids', [])
    return jsonify(controller.addMaladieToPatient(patient_id, maladie_ids))

@main_bp.route('/patients/<int:patient_id>/probabilites', methods=['GET'])
def patient_probabilites(patient_id):
    """
    Calcule la probabilité que le patient ait chaque maladie en fonction de ses symptômes.
    ---
    parameters:
      - name: patient_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Liste des probabilités par maladie
    """
    return jsonify(controller.maladieProbabilites(patient_id))