from flask import Blueprint, jsonify, request, send_file, make_response
from .controller import MainController
import io

main_bp = Blueprint('main', __name__)
controller = MainController()

@main_bp.route('/')
def index():
    return jsonify(controller.index())

@main_bp.route('/patients', methods=['GET'])
def patients():
    return jsonify(controller.getPatients())

@main_bp.route('/patients/nom/<string:nom>', methods=['GET'])
def patient_by_nom(nom):
    return jsonify(controller.getPatientByNom(nom))

@main_bp.route('/maladies', methods=['GET'])
def maladies():
    return jsonify(controller.getMaladies())

@main_bp.route('/maladies/nom/<string:nom>', methods=['GET'])
def maladie_by_nom(nom):
    return jsonify(controller.getMaladieByNom(nom))

@main_bp.route('/patients/<int:id>', methods=['GET'])
def patient_by_id(id):
    return jsonify(controller.getPatientById(id))

@main_bp.route('/maladies/<int:id>', methods=['GET'])
def maladie_by_id(id):
    return jsonify(controller.getMaladieById(id))

@main_bp.route('/patients', methods=['POST'])
def add_patient():
    from flask import request
    data = request.get_json()
    return jsonify(controller.addPatient(data))

@main_bp.route('/maladies', methods=['POST'])
def add_maladie():
    from flask import request
    data = request.get_json()
    return jsonify(controller.addMaladie(data))   

@main_bp.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    from flask import request
    data = request.get_json()
    return jsonify(controller.updatePatient(id, data))

@main_bp.route('/maladies/<int:id>', methods=['PUT'])
def update_maladie(id):
    from flask import request
    data = request.get_json()
    return jsonify(controller.updateMaladie(id, data))  

@main_bp.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    return jsonify(controller.deletePatient(id))  

@main_bp.route('/maladies/<int:id>', methods=['DELETE'])
def delete_maladie(id):
    return jsonify(controller.deleteMaladie(id))

@main_bp.route('/patients/<int:id>/maladies', methods=['GET'])
def patient_maladies(id):
    return jsonify(controller.patientMaladies(id))

@main_bp.route('/maladies/<int:id>/patients', methods=['GET'])
def maladie_patients(id):
    return jsonify(controller.maladiePatients(id))

@main_bp.route('/images', methods=['GET'])
def get_images():
    return jsonify(controller.getImages())

@main_bp.route('/images/<int:id>', methods=['GET'])
def get_image(id):
    return jsonify(controller.getImageById(id))

@main_bp.route('/images', methods=['POST'])
def add_image():
    file = request.files.get('data')
    url = request.form.get('url')
    description = request.form.get('description')
    maladie_id = request.form.get('maladie_id')
    data = file.read() if file else None

    return jsonify(controller.addImage(url, description, data, maladie_id))

@main_bp.route('/images/<int:id>/download', methods=['GET'])
def download_image(id):
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
    if not id:
        return jsonify({'message': 'Image ID is required'}), 400
    return jsonify(controller.deleteImage(id))

@main_bp.route('/patients/<int:patient_id>/maladies', methods=['POST'])
def add_maladies_to_patient(patient_id):
    data = request.get_json()
    maladie_ids = data.get('maladie_ids', [])
    return jsonify(controller.addMaladieToPatient(patient_id, maladie_ids))