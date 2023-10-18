from app import app
from app.api.errors import error_response
from app.api.auth import token_auth_error

# Mocked user for testing
class MockUser:
    def __init__(self, email):
        self.email = email

def test_token_auth_error():
    status = 401 
    with app.app_context():
        response = token_auth_error(status)
        expected_response = error_response(status)
    
    assert response.status == expected_response.status
