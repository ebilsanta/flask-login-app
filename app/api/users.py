from flask import jsonify, url_for, request, render_template
from flask_login import login_user
from flask_jwt_extended import create_access_token, decode_token
from smtplib import SMTPAuthenticationError
from app import db
from app.models import User
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request, unauthorized
from app.services.mail_service import send_email

@bp.route('/sign-up', methods=['POST'])
def sign_up():
    data = request.get_json() or {}
    required_fields = ['name', 'email', 'password', 'age', 'gender', 'image']

    if not all(field in data for field in required_fields):
        return bad_request('must include name, email, password, age, gender, image fields')

    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.login', id=user.id)
    return response

@bp.route("/login", methods=['POST'])
def login():
    data = request.get_json() or {}
    if not 'email' in data or not 'password' in data:
        return bad_request('must include email and password fields')

    email = data['email']
    password = data['password']

    user = User.query.filter_by(email=email).first()

    if not user:
        return unauthorized('user not found')

    if not user.check_password(password):
        return unauthorized('incorrect password')
    
    login_user(user)
    access_token = create_access_token(identity=user.email)

    response = jsonify(access_token=access_token)
    response.status_code = 200
    return response
    
@bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    url = request.host_url + 'reset-password/'
    data = request.get_json() or {}
    if not 'email' in data:
        return bad_request('must include email field')
    email = data['email']
    user = User.query.filter_by(email=email).first() 

    if not user:
        return bad_request("email not found")
    
    reset_token = create_access_token(identity=user.email)

    reset_url = url + reset_token

    try: 
        send_email(
            text_body="hello",
            sender="thaddeusleezx@gmail.com",
            subject='[Loginapp] Reset Your Password',
            recipients=[email],
            html_body=render_template('email/reset_password.html', user=user.name, url = url + reset_url)
        )
        response = jsonify(message="email sent")
    # in case email isn't set up properly
    except SMTPAuthenticationError as e:
        response = jsonify(
            reset_url = reset_url
        )

    response.status_code = 200
    return response


@bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json() or {}
    if not 'password' in data or not 'reset_token' in data:
        return bad_request('must include password and reset_token fields')
    reset_token = data['reset_token']
    password = data['password']
    user_email = decode_token(reset_token)['sub']
    
    user = User.query.filter_by(email=user_email).first()
    user.set_password(password)
    db.session.commit()
    response = jsonify(message="password changed successfully")
    response.status_code = 200
    return response


@bp.route('/me', methods=['GET'])
@token_auth.login_required
def me():
    return jsonify(token_auth.current_user().to_dict())


