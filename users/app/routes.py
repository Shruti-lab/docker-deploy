from app.users import user_bp
from flask import Blueprint, request, jsonify 
from flask_jwt_extended import jwt_required, get_jwt_identity
from pydantic import ValidationError
from app import db, bcrypt
from datetime import datetime
from app.models import User
from app.schema import UpdateUserSchema
import uuid
from app.utils.logger import get_logger


user_bp = Blueprint('user',__name__,url_prefix='/user')
logger = get_logger(__name__)


@user_bp.route('/aboutme')
@jwt_required()
def get_user_details():
    user_id = get_jwt_identity()
    user_id = uuid.UUID(user_id)
    try:
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"message":"User does not exist in users table."})

        return jsonify({"message":"Fetched user details successfully!",
        "data":{
            "user_id":user.id,
            "name":user.name,
            "email":user.email
        }})

    except Exception as e:
        logger.error(f"Database error during user detail fetch: {str(e)}")
        return jsonify({"message":f"Failed to fetch user details: {str(e)}"}), 500


@user_bp.route('/aboutme',methods=['PUT'])
@jwt_required()
def update_user_detail():
    user_id = get_jwt_identity()
    user_id = uuid.UUID(user_id)
    data = request.get_json()
    try:
        validated_data = UpdateUserSchema(**data)
    except ValidationError as e:
        logger.warning(f"Update user pydantic validation failed: {e.errors()}")
        return jsonify({"message":f"Update user pydantic validation failed: {str(e)}"}), 400
    
    try:   
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"message": "User not found."}), 404
        if validated_data.name is not None:
            user.name = validated_data.name
        if validated_data.password is not None:
            user.set_password(validated_data.password)

        return jsonify({
            "message":"Update successful!",
            "data":{
                "user_ id":user.id,
                "name":user.name,
                "email":user.email
            }
        }), 200

    except:
        logger.error(f"Database error during user update details: {str(e)}")
        return jsonify({"message":f"Failed to fetch user details: {str(e)}"}), 500


@user_bp.route('/health')
def health():
    return jsonify({"message":"Users microservice is working fine!"}), 200