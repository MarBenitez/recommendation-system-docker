# app/app.py

from flask import Flask
from .routes import main  # Cambiar a una importación relativa

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8081)
