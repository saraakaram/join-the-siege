from flask import Blueprint, request, jsonify

"""
This controller handles application health.
"""
health_bp = Blueprint('health', __name__)

@health_bp.route("/health_check", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200
