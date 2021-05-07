# Password Manager API

## Usage

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
    "id": "12",
    "username": "User",
    "email": "User@gmail.com",
    "public_id": "fed92080-51da-426f-a04b-603e773a6462",
    "permission_level": "normal"
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
    "id": "12",
    "username": "User1",
    "email": "User@gmail.com",
    "public_id": "fed92080-51da-426f-a04b-603e773a6462",
    "permission_level": "normal"
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