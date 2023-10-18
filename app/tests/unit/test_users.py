import os
from app import app
from flask_jwt_extended import create_access_token
from datetime import timedelta

def test_sign_up_invalid_data():
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    app.test = True
    with app.test_client() as test_client:
        data = {
            'name': 'Test User',
            'age': 25,
            'gender': 1,
            'image': 'test.jpg'
        }

    response = test_client.post('/api/sign-up', json=data)
    assert response.status_code == 400
    assert response.json['message'] == "must include name, email, password, age, gender, image fields"

def test_login_invalid_data():
    data = {'email': 'test@example.com'}
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    app.test = True
    with app.test_client() as test_client:
        response = test_client.post('/api/login', json=data)
    assert response.status_code == 400
    assert response.json['message'] == "must include email and password fields"

def test_forgot_password_user_not_found():
    data = {}
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    app.test = True
    with app.test_client() as test_client:
        response = test_client.post('/api/forgot-password', json=data)
    assert response.status_code == 400
    assert response.json['message'] == "must include email field"

def test_reset_password_invalid_data():
    data = {'password': 'newpassword'}
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    app.test = True
    with app.test_client() as test_client:
        response = test_client.post('/api/reset-password', json=data)
    assert response.status_code == 400
    assert response.json['message'] == 'must include password and reset_token fields'

def test_me_expired_token():
    data = {'email': 'test@example.com'}
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    app.test = True
    app.config['JWT_SECRET_KEY'] = 'TEST'
    
    expiration_time = timedelta(hours=-1)
    with app.test_client() as test_client:
        with app.app_context():
            access_token = create_access_token(identity=data['email'], expires_delta=expiration_time)
            headers = {'Authorization': 'Bearer ' + access_token}
            response = test_client.get('/api/me', headers=headers)
            assert response.status_code == 401
            assert response.json['msg'] == 'Token has expired'
