from flask_jwt_extended import decode_token
from flask_httpauth import HTTPTokenAuth
from app.services.users_service import get_user_by_email, UserNotFound
from app.api.errors import error_response

token_auth = HTTPTokenAuth()

@token_auth.verify_token
def verify_token(token):
    user_email = decode_token(token)['sub']
    try:
        user = get_user_by_email(user_email)
    except UserNotFound:
        return None
    return user
    
@token_auth.error_handler
def token_auth_error(status):
    return error_response(status)