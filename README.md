# Django Dans Waitlist

[![Lint](https://github.com/dan1229/django_dans_waitlist/actions/workflows/lint.yml/badge.svg)](https://github.com/dan1229/django_dans_waitlist/actions/workflows/lint.yml)
[![Test Python](https://github.com/dan1229/django_dans_waitlist/actions/workflows/test-python.yml/badge.svg)](https://github.com/dan1229/django_dans_waitlist/actions/workflows/test-python.yml)
[![codecov](https://codecov.io/gh/dan1229/django_dans_waitlist/branch/main/graph/badge.svg?token=TL09HDQWBJ)](https://codecov.io/gh/dan1229/django_dans_waitlist)

## Description

A Django app to handle waitlist and basic functionality.

Support for `Waitlist` and `WaitlistEntry` models, as well as a `WaitlistManager` to handle common operations.

## Quick start

1. Install the package via pip:

```bash
pip install django-dans-waitlist
```

2. Add "django_dans_waitlist" to your INSTALLED_APPS setting like this:

```python
INSTALLED_APPS = [
	...
	'django_dans_waitlist',
]
```

3. Include the URL configs in your project `urls.py` for the REST API endpoints like this:

```python
path("api/waitlist/", include("django_dans_waitlist.urls")),
```

4. Run `python manage.py migrate` to update your database schema.

5. Use the API endpoints, in code or your Django admin portal.

### Requirements

- Python 3.10 - 3.11
- Django 3.1 or higher
- Django Rest Framework
  - **NOTE:** not only must you have this installed, you must have set `DEFAULT_AUTHENTICATION_CLASSES` and `DEFAULT_PAGINATION_CLASS` in your `settings.py` to work with the APIs properly. An example config would be:

```python
REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
}
```


### Available Settings

Currently all available settings are optional:

- `TEAM_NAME` - Default team name to use for emails, can be added to message context manually as well still.


Add these to your `settings.py` file to customize the app's behavior like so:

```python
TEAM_NAME = "My Team"
```


## Usage

TODO

## Docs

TODO - which of these are still relevant?
#### [Model docs](https://github.com/dan1229/django_dans_waitlist/tree/main/docs/models.md).

#### [API docs](https://github.com/dan1229/django_dans_waitlist/tree/main/docs/apis.md).


-------------------------------------------------------

##### [https://danielnazarian.com](https://danielnazarian.com)

##### Copyright 2024 © Daniel Nazarian.

