from app.models import User

def test_user_creation():
    user = User(email='test@example.com', name='Test User', gender=1, age=25, image='test.jpg')
    user.set_password('testpassword')    
    
    assert user.email == 'test@example.com'
    assert user.name == 'Test User'
    assert user.gender == 1
    assert user.age == 25
    assert user.check_password('testpassword')
    assert user.image == 'test.jpg'

def test_user_to_dict():
    user = User(email='test@example.com', name='Test User', gender=1, age=25, image='test.jpg')
    user.set_password('testpassword')
    user_dict = user.to_dict()
    
    assert user_dict['email'] == 'test@example.com'
    assert user_dict['name'] == 'Test User'
    assert user_dict['gender'] == 1
    assert user_dict['age'] == 25
    assert user_dict['image'] == 'test.jpg'

def test_user_from_dict():
    user = User()
    user_data = {
        'email': 'test@example.com',
        'name': 'Test User',
        'gender': 1,
        'age': 25,
        'image': 'test.jpg',
        'password': 'testpassword'
    }
    user.from_dict(user_data, new_user=True)
    
    assert user.email == 'test@example.com'
    assert user.name == 'Test User'
    assert user.gender == 1
    assert user.age == 25
    assert user.image == 'test.jpg'
    assert user.check_password('testpassword')

