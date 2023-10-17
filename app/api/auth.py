from flask_jwt_extended import decode_token
from flask_httpauth import HTTPTokenAuth
from app.models import User
from app.api.errors import error_response

token_auth = HTTPTokenAuth()

@token_auth.verify_token
def verify_token(token):
    user_email = decode_token(token)['sub'] 
    user = User.query.filter_by(email=user_email).first()
    if user:
        return user
    return None
    
@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)