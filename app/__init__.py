# app/__init__.py

from flask import Flask
from .routes import main  # Cambiar a una importación relativa

def create_app():
    """Factory function to create and configure the Flask application."""
    app = Flask(__name__)

    # Register the blueprint with routes
    app.register_blueprint(main)

    return app
