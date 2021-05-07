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

### List all users

## Requires

`ADMIN = True`

`GET /users`