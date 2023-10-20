# Flask-login-app

A simple Flask backend with user login APIs  

Note to grader: I made a small refactoring change past the deadline at 9am, to extract duplicated database logic to a users_service. 

## Endpoints
### Sign Up
Creates a new user with given fields
- **Method**: `POST`
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
    - **error**: (string): `Bad Request` 
    - **message** (string)
      - `"Must include name, email and password fields"`

- **401 Unauthorized**
  - Response Body (JSON):
    - **error** (string): `Unauthorized`
    - **message** (string)
      - `"Email address in use"`

#### Sample Request
```
curl -i  --location --request POST 'http://localhost:5000/api/sign-up' \
--header 'Content-Type: application/json' \
--data-raw '{                         
    "email": "thaddeuslee3@gmail.com",
    "name": "thaddeusl",   
    "password": "abcd1234",
    "age": 2,   
    "gender": 0,                        
    "image": "http://www.image_link.com"
}
'
```
#### Sample Response
```
HTTP/1.1 201 CREATED
Server: Werkzeug/2.2.0 Python/3.8.17
Date: Fri, 20 Oct 2023 09:08:03 GMT
Content-Type: application/json
Content-Length: 116
Location: /api/login?id=4
Connection: close

{"age":2,"email":"thaddeuslee3@gmail.com","gender":0,"id":4,"image":"http://www.image_link.com","name":"thaddeusl"}
```

![Screenshot 2023-10-18 at 4 04 00 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/1e531330-0b11-4019-81a8-2965537b444d)
---

### Login
Authenticates user and returns JWT access token 
- **Method**: `POST`
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
    - **error**: (string): `Bad Request` 
    - **message** (string)
      - `"Must include name, email and password fields"`

- **401 Unauthorized**
  - Response Body (JSON):
    - **error** (string): `Unauthorized`
    - **message** (string)
      - `"Email not found"`
    OR
      - `"Incorrect password"`
   
#### Sample Request
```
curl -i --location --request POST 'http://localhost:5000/api/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "thaddeuslee3@gmail.com",
    "password": "abcd1234"
}'
```
#### Sample Response
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.0 Python/3.8.17
Date: Fri, 20 Oct 2023 09:11:14 GMT
Content-Type: application/json
Content-Length: 312
Vary: Cookie
Set-Cookie: session=.eJwlzj0OwjAMQOG7ZGZwEttJepnKv4K1pRPi7lTijW_6PmXPI85n2d7HFY-yv7xsRSyRNZq79oDOkzAFLdsApdpIOwzwBpF3ambE6GFQk32RZ6TXnHovMkjps7ILk_BgtoyQ0JEz0UWww8wVydNw9BFr6aRyQ64zjr8Gy_cHw14yUw.ZTJEMg.HX1pq0tJQXOiiiHcg9q_yyGjfEk; HttpOnly; Path=/
Connection: close

{"access_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5Nzc5MzA3NCwianRpIjoiZTU0Y2UzYjEtMjJhOC00M2Q2LWI2ZWEtYzJkMWI2YjdkMWI4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRoYWRkZXVzbGVlM0BnbWFpbC5jb20iLCJuYmYiOjE2OTc3OTMwNzQsImV4cCI6MTY5Nzc5NDI3NH0.FCMA_d-YXfN_C0Teu5B2n312N-KlEJo498LarJaLc5s"}
```

![Screenshot 2023-10-18 at 4 05 18 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/2f2078bf-e41d-44d7-873f-acdda255bdad)


---

### Forgot Password
Sends an email to the user with a link to reset password. If email service is not set up, it responds with the reset_url in the JSON body instead
- **Method**: `POST`
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
    - **error**: (string): `Bad Request` 
    - **message** (string)
      - `"Must include email fields"`

- **401 Unauthorized**
  - Response Body (JSON):
    - **error** (string): `Unauthorized`
    - **message** (string)
      - `"Email not found"`
   
#### Sample Request
```
curl -i --location --request POST 'http://localhost:5000/api/forgot-password' \
--header 'Content-Type: application/json' \
--data-raw '{
    "email": "thaddeusleezx@gmail.com"
}'
```

#### Sample Response 
* Email service set up
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.0 Python/3.8.17
Date: Fri, 20 Oct 2023 09:15:10 GMT
Content-Type: application/json
Content-Length: 25
Connection: close

{"message":"email sent"}
```

* Sample reset link with reset_token
```
http://localhost:5000/reset-password/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5Nzc5MzgwOCwianRpIjoiMTI4NWRjOTMtNTkzZC00NmZhLTgwZGItMTNmNDI1NjgwNWFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRoYWRkZXVzbGVlenhAZ21haWwuY29tIiwibmJmIjoxNjk3NzkzODA4LCJleHAiOjE2OTc3OTUwMDh9._wPVgTVbKlPxeIgFdIq0d2F6UAW0EZWejSx33Otgi7U
```

![Screenshot 2023-10-18 at 4 05 39 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/07a20c4c-f171-4c5c-af5f-483c2140a382)

<img width="1174" alt="Screenshot 2023-10-18 at 9 07 46 AM" src="https://github.com/ebilsanta/flask-login-app/assets/101983505/9991016a-8542-465f-91c6-5d3027fd31c0">

---

### Reset Password

- **Method**: `POST`
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
    - **error**: (string): `Bad Request` 
    - **message** (string)
      - `"Must include password and reset_token fields"`

- **401 Unauthorized**
  - Response Body (JSON):
    - **error** (string): `Unauthorized`
    - **message** (string)
      - `"Email not found"`
   
      
![Screenshot 2023-10-18 at 4 06 48 AM](https://github.com/ebilsanta/flask-login-app/assets/101983505/61989e32-7ecc-42ae-b404-4c1dfc2b5e10)
#### Sample Request
```
curl -i --location --request POST 'http://localhost:5000/api/reset-password' \
--header 'Content-Type: application/json' \
--data-raw '{
    "password": "newpassword",
    "reset_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5Nzc5MzgwOCwianRpIjoiMTI4NWRjOTMtNTkzZC00NmZhLTgwZGItMTNmNDI1NjgwNWFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRoYWRkZXVzbGVlenhAZ21haWwuY29tIiwibmJmIjoxNjk3NzkzODA4LCJleHAiOjE2OTc3OTUwMDh9._wPVgTVbKlPxeIgFdIq0d2F6UAW0EZWejSx33Otgi7U"
}'
```

#### Sample Response
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.0 Python/3.8.17
Date: Fri, 20 Oct 2023 09:28:19 GMT
Content-Type: application/json
Content-Length: 44
Connection: close

{"message":"password changed successfully"}
```
---

### Get Current User (Me)

- **Method**: `GET`
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

#### Sample Request
```
curl -i --location --request GET 'http://localhost:5000/api/me' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5Nzc5NDIzOCwianRpIjoiOGJkMzFlZWEtMDFhOS00MDMzLTk0MjItMGJmZmFjNTk5YjA1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRoYWRkZXVzbGVlM0BnbWFpbC5jb20iLCJuYmYiOjE2OTc3OTQyMzgsImV4cCI6MTY5Nzc5NTQzOH0.s1YqSw_y8ZAXR9_DpyHKHv-0gGam9DbSTo7izZzBXQc'
```

#### Sample Response
```
HTTP/1.1 200 OK
Server: Werkzeug/2.2.0 Python/3.8.17
Date: Fri, 20 Oct 2023 09:31:30 GMT
Content-Type: application/json
Content-Length: 116
Connection: close

{"age":2,"email":"thaddeuslee3@gmail.com","gender":0,"id":4,"image":"http://www.image_link.com","name":"thaddeusl"}
```

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
python3.8 -m venv .venv
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

Create a copy of .flaskenv.sample, set up environment variables and rename it to .flaskenv
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

Reload shell configuration (I have to do this if not I'll get an error running migrations)
* for Bash
```
source ~/.bashrc
```
* for Zsh
```
source ~/.zshrc
```

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
* Please check that you're using Python 3.8.17, I ran into problems using newer versions.  
* Check also that your virtual environment is activated
```
which python
```
should show the path to your virtual environment
* Restart your IDE if using an integrated terminal  
* Otherwise, please email me at thaddeusleezx@gmail.com :)

## Future roadmap
* Implement a refresh token endpoint instead of requiring user to log in again, will need some level of security such as HttpOnly cookies
* Implement proper image uploading instead of image link, using object storages like Amazon S3
* Add test cases for database layer

