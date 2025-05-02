from flask import Blueprint, request, jsonify
from src.services.file_service import allowed_file, is_valid, process_file
from src.services.classification_service import classify_file

"""
This controller handles file-related endpoints.
"""
file_bp = Blueprint('file', __name__)

@file_bp.route('/classify_file', methods=['POST'])
def classify_file_route():
    """
    Endpoint to classify uploaded files
    Returns the predicted document class or error message.
    """

    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": f"File type not allowed"}), 400

    # TODO: Modify this after implementing new classification method
    file_text = process_file(file)
    file_class = classify_file(file)
    return jsonify({"file_class": file_class}), 200