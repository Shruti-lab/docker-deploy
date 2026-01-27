from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity
from app import db
import logging
from datetime import datetime
from app.models.user_models import User
from app.models.admin_models import Admin
from app.utils.adminCheck import admin_required
from app.schema.user_schema import CreateUserSchema
from app.schema.auth_schema import SignUpSchema
from pydantic import ValidationError
import uuid


admin_bp = Blueprint('admin',__name__,url_prefix='/admin')
logger = logging.getLogger(__name__)



@admin_bp.route('/signup',methods=['POST'])
def signup():
    data = request.get_json()
    try:
        validated_data = SignUpSchema(**data)
    except ValidationError as e:
        logger.warning(f"Signup pydantic validation failed: {e.errors()}")
        return jsonify({"message":f"Signup pydantic validation failed: {str(e)}"}), 400

    existing_admin = Admin.query.filter_by(email=validated_data.email).first()
    if existing_admin:
        return jsonify({"message": "Admin email already registered"}), 400
    
    try:   
        new_admin = Admin(
            name = validated_data.name,
            email = validated_data.email
        )
        new_admin.set_password(validated_data.password)
        db.session.add(new_admin)
        db.session.commit()

        return jsonify({
            "message":"Admin registered successfully",
            "admin_id":new_admin.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        logger.error(f"Database error during admin signup: {str(e)}")
        return jsonify({"message":f"New admin signup failed: {str(e)}"}), 500





@admin_bp.route('/users',methods=['POST'])
@admin_required
def create_user():
    admin_id = get_jwt_identity()
    data = request.get_json()
    try:
        user_data = CreateUserSchema(**data)
    except ValidationError as e:
        return jsonify({"error":e.errors()}), 400
    
    # Check if the user email already exissts
    existing_user = User.query.filter_by(email=user_data.email).first()
    if existing_user:
        return jsonify({"message":"User already exists."})

    try:
        new_user = User(
            name=user_data.name,
            email=user_data.email,
            admin_id = admin_id
        )
        new_user.set_password(user_data.password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"New user created successfully",
        "data":{
            "user_id":new_user.id,
            "name":new_user.name,
            "email":new_user.email
        }}), 201
    except Exception as e:
        db.session.rollback()
        logger.error(f"Database error during user creation: {str(e)}")
        return jsonify({"message":f"New user creation failed: {str(e)}"}), 500


@admin_bp.route('/users')
@admin_required
def get_users():
    admin_id = get_jwt_identity()
    try:
        users = User.query.filter_by(admin_id=admin_id).all()
        return jsonify({
            "message":"Users fetched successfully",
            "data":[user.to_dict() for user in users],
            "length":len(users)
        }), 200
    except Exception as e:
        logger.error(f"Database error during users fetch: {str(e)}")
        return jsonify({"message":f"Failed to fetch users: {str(e)}"}), 500


# Get one user
# @admin_bp.routes('/users',methods=['PUT'])
# @admin_required
# def update_user_detail():
#     admin_id = get_jwt_identity()
#     data = request.get_json()
#     try:
#         user = User.query.
#     except Exception as e:


@admin_bp.route('/users/<user_id>',methods=['DELETE'])
@admin_required
def delete_user(user_id):
    admin_id = get_jwt_identity()

    try:
        user_id = uuid.UUID(user_id)
        admin_id = uuid.UUID(admin_id)
    except ValueError:
        return jsonify({"message": "Invalid UUID format"}), 400
    
    try:
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return jsonify({"message": "User not found"}), 404
        if user.admin_id and user.admin_id != admin_id:
            return jsonify({"message": "Not authorized to delete this user"}), 403
        
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": "User deleted successfully"}), 200

    except Exception as e:
        logger.error(f"Database error during user delete: {str(e)}")
        return jsonify({"message":f"Failed to delete user: {str(e)}"}), 500



@admin_bp.route('/health')
def health():
    return jsonify({"message":"Admin microservice is working fine!"}), 200




    
