from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db, bcrypt
import logging
from datetime import datetime
from app.schema.auth_schema import LoginSchema
from app.models.admin_models import Admin
from app.models.user_models import User
from app.utils.jwtUtil import generate_jwt


auth_bp = Blueprint('auth',__name__,url_prefix='/auth')
logger = logging.getLogger(__name__)


@auth_bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()

    try:
        validated_data = LoginSchema(**data)
    except ValidationError as e:
        logger.warning(f"Login pydantic validation failed: {e.errors()}")
        return jsonify({"message":f"Login pydantic validation failed: {str(e)}"}), 400


    if validated_data.role == 'admin':
        admin = Admin.query.filter_by(email=validated_data.email).first()
        if admin and admin.check_password(validated_data.password):
            token = generate_jwt(admin.id, role="admin")
            return jsonify({
                "message":"Admin logged in successfully!",
                "access_token": token,
                "role": "admin"
            }), 200
        else:
            return jsonify({"message": "Invalid email or password"}) , 401
    
    if validated_data.role == 'user':
        user = User.query.filter_by(email=validated_data.email).first()
        if user and user.check_password(validated_data.password):
            token = generate_jwt(user.id, role="admin")
            return jsonify({
                "message":"User logged in successfully!",
                "access_token": token,
                "role": "user"
            }), 200
        else:
            return jsonify({"message": "Invalid email or password"}) , 401
    


    
    

    



