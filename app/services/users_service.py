from app import db
from app.models import User

class UserAlreadyExists(Exception):
    pass

class UserNotFound(Exception):
    pass

def save_new_user(data):
    if User.query.filter_by(email=data['email']).first():
        raise UserAlreadyExists("User with this email already exists")

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    return user

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def update_user_password(user_email, new_password):
    user = get_user_by_email(user_email)
    if not user:
        raise UserNotFound("User with this email does not exist")
    user.set_password(new_password)
    db.session.commit()
    return user