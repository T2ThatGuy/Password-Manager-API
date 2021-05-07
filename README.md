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

All responses will be in the form

```json
{
    "data": "Holds the content of the response",
    "message": "Description of the response"
}
```

Subsequent response definitions will only detail the expected value fo the `data field`

### Register a New User

**Requires**

`USAGE : POST /user/signup`

**Arguments**

- `"username":string`
- `"email":string`
- `"password":string`

**Response**

- `201 Created` on success

```json
{
    "data": {
        "id": "12",
        "username": "User",
        "email": "User@gmail.com",
        "public_id": "fed92080-51da-426f-a04b-603e773a6462",
        "permission_level": "normal"
    },
    "token": "Generated Session Token"
}
```

### Login a User

**Requires**

`USAGE : GET /user/login`

**Arguments / Authentication**

- `"Username / Email":string`
- `"Password":string`

**Response**

- `200 OK` on success
- `401 Unauthorized` on failed login attempt

```json
If Successful

{
    "data": {
        "id": "12",
        "username": "User",
        "email": "User@gmail.com",
        "public_id": "fed92080-51da-426f-a04b-603e773a6462",
        "permission_level": "normal"
    },
    "token": "Generated Session Token"
}
```

### Update user password

**Requires**

`USAGE : PUT /user/update-password`

**Arguments**

- `"id":string` Non public version of the users ID
- `"password":string` New password for the user

**Response**

- `200 OK` on success
- `404 Not Found or 401 Unauthorized` on failed password update

## Admin Usage

### List all users

**Requires**

`PERMISSION LEVEL : ADMIN`

`USAGE : GET /user`

**Response**

- `200 OK` on success

```json
[
    {
        "username": "User1",
        "email": "User1@gmail.com",
        "public_id": "fed92080-51da-426f-a04b-603e773a6462",
        "permission_level": "normal"
    },
    {
        "username": "User2",
        "email": "User2@gmail.com",
        "public_id": "3017fa41-574d-4be6-98ba-951a5dfa2a16",
        "permission_level": "admin"
    }
]
```