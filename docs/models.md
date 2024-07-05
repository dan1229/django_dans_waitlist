# Models

The model setup for this app is simple and straightforward. There are two main models: `AbstractBaseModel` and `WaitlistEntry`.

## AbstractBaseModel

This is an abstract base model that provides common fields for all other models in the app.

### Fields

- **id**: `UUIDField` - Primary key for the model, automatically generated.
- **datetime_created**: `DateTimeField` - Timestamp for when the record was created, automatically set on creation.
- **datetime_modified**: `DateTimeField` - Timestamp for when the record was last modified, automatically updated on save.

## WaitlistEntry

Representation of a single entry in the waitlist. Inherits from `AbstractBaseModel`.

### Fields

- **email**: `EmailField` - Email address of the user, must be unique.

## Summary

- The `AbstractBaseModel` provides common fields and behavior for other models.
- The `WaitlistEntry` model represents an entry in the waitlist and includes an email field.

For more details on these models, refer to `models.py` in the source code.

-------------------------------------------------------

##### [https://danielnazarian.com](https://danielnazarian.com)

##### Copyright 2024 © Daniel Nazarian.