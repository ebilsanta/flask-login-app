# Flask-login-app

A simple Flask backend with user login APIs

## Endpoints
### Sign Up
Creates a new user with given fields
- **Method**: POST
- **Endpoint**: `/api/sign-up`

#### Request

##### Body (JSON)

- **name** (string): User's name.
- **email** (string): User's email address.
- **password** (string): User's password.
- **age** (integer): User's age.
- **gender** (integer): User's gender.
- **image** (string): URL or path to user's profile image.

#### Responses

- **201 Created**
  - Response Body (JSON):
    - **id** (integer): User ID.
    - **email** (string): User's email address.
    - **name** (string): User's name.
    - **age** (integer): User's age.
    - **gender** (integer): User's gender.
    - **image** (string): URL or path to user's profile image.

- **400 Bad Request**
  - Response Body (JSON):
    - **error** (string): Error message.

![Screenshot 2023-10-18 at 4 04 00 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/1e531330-0b11-4019-81a8-2965537b444d)
---

### Login
Authenticates user and returns JWT access token 
- **Method**: POST
- **Endpoint**: `/api/login`

#### Request

##### Body (JSON)

- **email** (string): User's email address.
- **password** (string): User's password.

#### Responses

- **200 OK**
  - Response Body (JSON):
    - **access_token** (string): JWT access token.

- **400 Bad Request**
  - Response Body (JSON):
    - **error** (string): Error message.

- **401 Unauthorized**
  - Response Body (JSON):
    - **error** (string): Error message.
![Screenshot 2023-10-18 at 4 05 18 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/2f2078bf-e41d-44d7-873f-acdda255bdad)

---

### Forgot Password
Sends an email to the user with a link to reset password. If email service is not set up, it responds with the reset_url in the JSON body instead
- **Method**: POST
- **Endpoint**: `/api/forgot-password`

#### Request

##### Body (JSON)

- **email** (string): User's email address.

#### Responses

- **200 OK**
  - Response Body (JSON):
    - **message** (string): Success message.

- **400 Bad Request**
  - Response Body (JSON):
    - **error** (string): Error message.
![Screenshot 2023-10-18 at 4 05 39 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/07a20c4c-f171-4c5c-af5f-483c2140a382)

---

### Reset Password

- **Method**: POST
- **Endpoint**: `/api/reset-password`

#### Request

##### Body (JSON)

- **password** (string): New password.
- **reset_token** (string): Token for password reset, obtained from the email or response from the forgot-password endpoint

#### Responses

- **200 OK**
  - Response Body (JSON):
    - **message** (string): Success message.

- **400 Bad Request**
  - Response Body (JSON):
    - **error** (string): Error message.
![Screenshot 2023-10-18 at 4 06 48 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/61989e32-7ecc-42ae-b404-4c1dfc2b5e10)

---

### Get Current User (Me)

- **Method**: GET
- **Endpoint**: `/api/me`

#### Request

- Requires authentication with a valid JWT token.
- Add the access_token from /login in the Authorization header as "Bearer <token>"

#### Responses

- **200 OK**
  - Response Body (JSON):
    - User details (id, email, name, age, gender, image).

- **401 Unauthorized**
  - Response Body (JSON):
    - **error** (string): Error message.
![Screenshot 2023-10-18 at 4 07 12 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/3279c0d1-2941-4a08-ba1a-b0ce620698f4)


## Getting Started

### Dependencies

* Python 3.8.17

### Executing program

Clone the repository
```
git clone https://github.com/ebilsanta/flask-login-app
```

Create a virtual environment
```
python3 -m venv .venv
```

Activate the virtual environment  
* For windows:
```
.venv\Scripts\activate
```

* For Mac/Linux:
```
source .venv/bin/activate
```

Change directory 
```
cd flask-login-app
```

Install packages from requirements.txt
```
pip install -r requirements.txt
```

Set up environment variables in .flaskenv.sample and rename it to .flaskenv
```
FLASK_APP=loginapp
SECRET_KEY=<your-secret-key-here>
JWT_SECRET_KEY=<your-jwt-secret-key-here>
MAIL_USERNAME=<your-gmail-username-here>
MAIL_PASSWORD=<your-gmail-app-password>
```
- The SECRET_KEY and JWT_SECRET_KEY can be arbitrary values.
- JWT_SECRET_KEY is used by flask_jwt_extended package to generate access_tokens.
- The MAIL_USERNAME and MAIL_PASSWORD are used to authenticate with your email provider to send emails for the forgot-password endpoint. 
For Google, you cannot use your raw password and will have to request for an app password from [Google] (https://support.google.com/accounts/answer/185833?hl=en)

Run database migrations
```
flask db upgrade
```

Start flask app
```
flask run
```

The app should now be live at (http://localhost:5000)!

### Testing
Tests can be run using
```
python3 -m pytest
```
![Screenshot 2023-10-18 at 4 07 51 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/3ea3865b-eaf4-4cee-957d-4f5398277e38)

### Troubleshooting
Please check that you're using Python 3.8.17, I ran into problems using newer versions.  
Otherwise, please email me at thaddeusleezx@gmail.com :)

## Future roadmap
* Add a frontend by refactoring code to have routes and templates that use the API logic
* Implement a refresh token endpoint instead of requiring user to log in again, will need some level of security such as HttpOnly cookies
* Implement proper image uploading instead of image link, using object storages like Amazon S3

