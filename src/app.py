from flask import Flask
from src.controllers.file_controller import file_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(file_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
