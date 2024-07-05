# APIs

This document provides an overview of the available API endpoints for interacting with the waitlist functionality in the Django Dans Waitlist package.

## Waitlist Entries

### Create a Waitlist Entry

- **Endpoint**: `/entries/`
- **Method**: POST
- **Parameters**:
  - `email` (string, required): The email address to be added to the waitlist.

#### Example Request

```http
POST /entries/
Content-Type: application/json

{
  "email": "user@example.com"
}
```

#### Example Response

```
HTTP/1.1 201 Created
Content-Type: application/json

{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "user@example.com",
  "datetime_created": "2024-07-04T12:34:56.789Z",
  "datetime_modified": "2024-07-04T12:34:56.789Z"
}
```

## Basic

Send Emails to Waitlist Entries

	•	Endpoint: /entries/emails/
	•	Method: POST
	•	Parameters:
	•	message (string, required): The message to be sent to the waitlist entries.
	•	subject (string, optional): The subject of the email. If not provided, a default subject will be used.

### Send Emails to Waitlist Entries

- **Endpoint**: `/entries/emails/`
- **Method**: POST
- **Parameters**:
  - `message` (string, required): The message to be sent to the waitlist entries.
  - `subject` (string, optional): The subject of the email. If not provided, a default subject will be used.

#### Example Request

```http
POST /entries/emails/
Content-Type: application/json

{
  "message": "Welcome to the waitlist!",
  "subject": "Waitlist Update"
}
```

#### Example Response

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "message": "Successfully sent message(s)!"
}
```

### Error Handling

For both endpoints, the API will return appropriate error messages in case of invalid input or other issues.

#### Example Error Response

```
HTTP/1.1 400 Bad Request
Content-Type: application/json

{
  "message": "Error. Please try again later.",
  "error_fields": {
    "email": ["Invalid email format."]
  }
}
```

