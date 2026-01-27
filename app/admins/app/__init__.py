from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from app.config import Config
from flask_migrate import Migrate
from app.database import db

bcrypt = Bcrypt()
jwt = JWTManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app,db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from app.models import User, Admin

    from app.routes import admin_bp
    app.register_blueprint(admin_bp)

    @app.route('/')
    def test_app():
        return jsonify({"message":"The flask application is running fine!"}) , 200

    @app.route('/health')
    def health():
        return jsonify({"message":"Health of application is good."}) , 200



    return app

