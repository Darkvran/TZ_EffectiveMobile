from flask import Flask
from app.models import db

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///TZeffective.db"
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
