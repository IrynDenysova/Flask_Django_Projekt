# app/__init__.py
from flask import Flask
from app.extentions import db, migrate
from app.routers.questions import questions_bp
from app.routers.response import response_bp
from app.routers.category import categories_bp
from config import DevelopmentConfig
import app.models


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(questions_bp, url_prefix='/questions')
    app.register_blueprint(response_bp, url_prefix='/response')
    app.register_blueprint(categories_bp, url_prefix='/categories')
    return app
