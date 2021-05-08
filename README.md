# Password Manager API

## Creating / Linking a Database

After downloading the repository the database will not exist yet. You will have to create the database using the models provided in the database.py file.

This can be done through the following terminal / cmd commands

- `Navigate to the root dir of the project`
- `python` to open the python shell in the console
- `from app.database import db` to import the database functionality
- `db.create_all()` to create the database and its file

To check that the database file has been correctly created navigate to the app folder and you should see the `database.db` this is your database file.

If this does not work or returns an error at any stage make sure you have the SQLAlchemy extension library for Flask installed!

## Normal Usage

All responses will resemble this form
```json
{
    "data": "Holds the content of the response",
    "message": "Desciption of the response"
}
```

Responses below will only detail the contents of the `data` field

All requests will require a piece of JSON attached to be used in the request unless stated otherwise in the specific request... The content of the JSON required can be found in each requests arguments section below.

## User Routes

### Resiter a new user

**Requires**

`USAGE : POST /user/signup`

**Arguments**

- `"username":string`
- `"email":string`
- `"password":string`

**Response**

- `201 Created` on success
- `400 Failed` on failure

```json
{
    "data": {
        "id": "ID of the new user (int)",
        "username": "Username of the new user (string)",
        "email": "Email of the new user (string)",
        "public_id": "Public ID of the new user (string)",
        "admin": "Admin status of the new user (boolean)",
        "token": "Valid token of the new user (string) lasting a set time before timing out"
    }
}
```

### Login a user

**Requires**

`USAGE : GET /user/login`

**Arguments / Authentication**

- `"Username":string`
- `"Password":string`

**Response**

- `200 OK` on success
- `401 Unauthorized` on failed login attempt

```json
{
    "data": {
        "id": "ID of the new user (int)",
        "username": "Username of the new user (string)",
        "email": "Email of the new user (string)",
        "public_id": "Public ID of the new user (string)",
        "admin": "Admin status of the new user (boolean)",
        "token": "Valid token of the new user (string) lasting a set time before timing out"
    }
}
```

### Change user password

**Requires**

`USAGE : PUT /user/update-password`

**Required Header Value**

- `"x-access-token":string` Previously given token upon user login or sign up

**Response**

- `200 OK` on success
- `401 Unauthorized` on invalid token

```json
{
    "data": [],
    "message": "Password Updated Successfully!"
}
```

## Dashboard Routes

### Create password form

### Delete password form

### Change password form

### Get all passwords for a specific user

### Get a specific password