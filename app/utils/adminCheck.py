from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt, decode_token

# Custom decorator
def admin_required(func):
    @jwt_required()
    @wraps(func)
    def wrapper(*args,**kwargs):
        claims = get_jwt()
        if claims.get('role')!='admin':
            return jsonify({"message":"Unauthorized, ONLY Admin can access"}) , 403
        return func(*args,**kwargs)
    return wrapper

