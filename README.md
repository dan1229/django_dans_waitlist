# Django Dans Waitlist


[![Lint](https://github.com/dan1229/django_dans_waitlist/actions/workflows/python-lint.yml/badge.svg)](https://github.com/dan1229/django_dans_waitlist/actions/workflows/python-lint.yml)
[![Test](https://github.com/dan1229/django_dans_waitlist/actions/workflows/python-test.yml/badge.svg)](https://github.com/dan1229/django_dans_waitlist/actions/workflows/python-test.yml)
[![Types](https://github.com/dan1229/django_dans_waitlist/actions/workflows/python-types.yml/badge.svg)](https://github.com/dan1229/django_dans_waitlist/actions/workflows/python-types.yml)
[![codecov](https://codecov.io/gh/dan1229/django_dans_waitlist/branch/main/graph/badge.svg?token=TL09HDQWBJ)](https://codecov.io/gh/dan1229/django_dans_waitlist)

[![Python Versions](https://img.shields.io/pypi/pyversions/django-dans-waitlist.svg?color=3776AB&logo=python&logoColor=white)](https://www.python.org/)
[![Django Versions](https://img.shields.io/pypi/djversions/django-dans-waitlist?color=0C4B33&logo=django&logoColor=white&label=django)](https://www.djangoproject.com/)
[![PyPI Version](https://img.shields.io/pypi/v/django-dans-waitlist.svg?color=blue&logo=pypi&logoColor=white)](https://pypi.org/project/django-dans-waitlist/)
[![Downloads](https://static.pepy.tech/badge/django-dans-waitlist/month)](https://pepy.tech/project/django-dans-waitlist)
[![GitHub stars](https://img.shields.io/github/stars/dan1229/django-dans-waitlist?logo=github&style=flat)](https://github.com/dan1229/django-dans-waitlist/stargazers)
[![License](https://img.shields.io/pypi/l/django-dans-waitlist.svg?color=blue)](https://github.com/dan1229/django-dans-waitlist/blob/main/LICENSE.txt)
[![Codacy grade](https://img.shields.io/codacy/grade/21cb657283c04e70b56fb935277a1ad1?logo=codacy)](https://www.codacy.com/app/dan1229/django-dans-waitlist)
[![Code style](https://img.shields.io/badge/code%20style-black-000000.svg?logo=python&logoColor=black)](https://github.com/psf/black)

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


## Docs

#### [Model docs](https://github.com/dan1229/django_dans_waitlist/tree/main/docs/models.md).

#### [API docs](https://github.com/dan1229/django_dans_waitlist/tree/main/docs/apis.md).


-------------------------------------------------------

##### [https://danielnazarian.com](https://danielnazarian.com)

##### Copyright 2024 © Daniel Nazarian.

