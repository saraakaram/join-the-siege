from flask import Flask
from src.controllers.file_controller import file_bp
from src.controllers.application_controller import health_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(file_bp)
    app.register_blueprint(health_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
