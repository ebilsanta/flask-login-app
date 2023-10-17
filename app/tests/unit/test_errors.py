from app import app
from app.api.errors import error_response, bad_request, unauthorized

def test_error_response():
    status_code = 404
    message = "Not Found"
    with app.app_context():
        response = error_response(status_code, message)

    assert response.status_code == status_code
    assert response.json == {'error': 'Not Found', 'message': message}

def test_bad_request():
    message = "Bad Request"

    with app.app_context():
        response = bad_request(message)

    assert response.status_code == 400
    assert response.json == {'error': 'Bad Request', 'message': message}

def test_unauthorized():
    message = "Unauthorized"
    with app.app_context():
        response = unauthorized(message)

    assert response.status_code == 401
    assert response.json == {'error': 'Unauthorized', 'message': message}
