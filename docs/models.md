# Models

TODO UPDATE

To use this package simply utilize the models included as well as their properties/helper methods. This document is meant to help illustrate the differences between the different types of notifications.

## `NotificationBase`

ALL notifications inherit from `NotificationBase` and thus all have the following properties:

- `recipients` - comma separated list of emails the notification was sent to.
- `sender` - email of the sending user.
- `datetime_sent` - date time the notification was sent.
- `sent_successfully` - whether the notification was processed correctly.

## `NotificationEmail`

- Meant to track emails sent.
- Email templates included, editable via context variables
    - `NotificationEmailTemplate` model - see `email-template.md` for more info.
    - Admin editable templates and emails
- `send_email` function to actually send emails and handle object creation.
    - `NotificationEmail.objects.send_email(...)`

## `NotificationBasic`

- Meant to model a generic notification stack internal to the application i.e., a notification stack in your application.
- Has a 'read' property

## `NotificationPush`

- Track push notifications that may require extra information.

