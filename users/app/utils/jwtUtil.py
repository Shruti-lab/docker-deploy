from flask_jwt_extended import create_access_token
from datetime import timedelta

def generate_jwt(id, role, expires_delta=timedelta(hours=10)):
    access_token = create_access_token(identity=id, additional_claims ={'role':role} ,expires_delta=expires_delta)
    return access_token
