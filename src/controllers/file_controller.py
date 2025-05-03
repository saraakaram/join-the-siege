from flask import Blueprint, request, jsonify
from src.services.file_service import get_file_extension, is_valid, process_file
from src.services.model_service import ModelService

"""
This controller handles file-related endpoints.
"""
file_bp = Blueprint('file', __name__)
model_service = ModelService.get_instance()

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

    file_extension = get_file_extension(file.filename)
    if not is_valid(file_extension):
        return jsonify({"error": f"File type not allowed"}), 400

    file_text = process_file(file, file_extension)

    if not file_text:
        return jsonify({"error": f"Document content not found"}), 400
    
    file_class = model_service.classify_file(file_text)
    return jsonify({"file_class": file_class}), 200

@file_bp.route("/add_class", methods=["POST"])
def add_file_type():
    """
    Endpoint to add new file types (new classes)
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    sample_file = request.files['file']
    file_type = request.form.get('file_type', '').strip().lower()

    if not file_type or sample_file.filename == '':
        return jsonify({"error": "File type and file are required."}), 400

    file_extension = get_file_extension(sample_file.filename)
    if not is_valid(file_extension):
        return jsonify({"error": "File type not allowed"}), 400

    file_text = process_file(sample_file, file_extension)
    if not file_text:
        return jsonify({"error": f"Document content not found"}), 400
    
    try:
        model_service.embed_file(file_type, file_text)
        return jsonify({"message": f"File type '{file_type}' registered successfully."}), 200
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500