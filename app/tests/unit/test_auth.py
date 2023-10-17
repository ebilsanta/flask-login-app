from app import app
from app.api.errors import error_response
from app.models import User
from app.api.auth import verify_token, token_auth, token_auth_error
from flask_jwt_extended import create_access_token

# Mocked user for testing
class MockUser:
    def __init__(self, email):
        self.email = email

def test_verify_token():
    app.config['JWT_SECRET_KEY'] = 'test'
    with app.app_context():
        user_email = 'test@example.com'
        token = create_access_token(identity=user_email)
        user = MockUser(user_email)
        
        def decode_token_mock(token):
            return {'sub': user_email}
        
        def filter_by_mock(email):
            return user
        
        token_auth._decode_token = decode_token_mock
        User.query.filter_by = filter_by_mock
        
        verified_user = verify_token(token)
        
    assert verified_user.email == user.email

def test_token_auth_error():
    status = 401 
    with app.app_context():
        response = token_auth_error(status)
        expected_response = error_response(status)
    
    assert response.status == expected_response.status
