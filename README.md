# DRF Problems [![PyPI version](https://badge.fury.io/py/drf-problems.svg)](https://badge.fury.io/py/drf-problems) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/815f1503809749c3a6b61d129dbb1c1a)](https://www.codacy.com/manual/shivanshs9/drf-problems?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=shivanshs9/drf-problems&amp;utm_campaign=Badge_Grade) [![Downloads](https://pepy.tech/badge/drf-problems)](https://pepy.tech/project/drf-problems) [![HitCount](https://hits.dwyl.com/shivanshs9/drf-problems.svg)](http://hits.dwyl.com/shivanshs9/drf-problems)

## TL;DR

This library implements [RFC 7807](https://tools.ietf.org/html/rfc7807) in our favorite Django REST Framework! Or, in layman terms, it introduces "Problem Details" in the HTTP APIs.

## Table of Contents

- [Features](#features)
- [Pre-Requisites](#pre-requisites)
- [Installation](#installation)
- [Usage](#usage)
  - [With exceptions](#with-exceptions)
  - [With permissions](#with-permissions)
  - [With Views](#with-views)
- [Resources](#resources)
- [Roadmap](#roadmap)
- [Contributing](#contributing)

## Features

- Handles exception to return response with Problem Details model.
- Added permission mixins and base class to store exception to raise by the view on failure of permission.
- Added view mixin which throws exception of failed permission.
- These permissions are compatible with composable permissions introduced in DRF 3.9.0!
- Has problem description endpoint to understand about the problem with the given code.
- Has sample permissions which checks for minimum API version.

## Pre-Requisites

- Django >= 2.0 (Tested with 2.2)
- djangorestframework >= 3.0.0 (Tested with 3.9.0)

## Installation

Install the library as you would for any django library.

- Install using pip.
  `pip install drf-problems`
- Add 'drf_problems' to your **INSTALLED_APPS** setting.

```python
INSTALLED_APPS = (
    ...
    'drf_problems',
)
```

- DRF's default exception handler needs to be replaced. In your `settings.py`, update:

```python
REST_FRAMEWORK = {
    ...
    'EXCEPTION_HANDLER': 'drf_problems.exceptions.exception_handler',
```

- To use the problem description url, you need to update your `urls.py`:

```python
urlpatterns = [
    ...
    path('', include('drf_problems.urls'))
]
```

## Usage

### With exceptions

In your exception class, define `default_code` with the error code string which is used in the type URI.
To set custom title, define `title` with the human-readable summary of the problem type.
To set description, define `description` with a long paragraph describing the problem.

Finally, make sure to register your exception with `drf_problems.utils.register_exception` function or `drf_problems.utils.register` decorator.
Here's a sample exception class:

```python
from drf_problems.utils import register_exception, register

@register # Either use this decorator
class InvalidVersionRequestedException(exceptions.NotAcceptable):
    default_code = 'invalid_version'
    title = 'Invalid API version'
    default_detail = 'Provided API version is invalid.')
    description = 'Malformed or unsupported version string is provided with the request.'

register_exception(InvalidVersionRequestedException) # Or this method directly.
```

### With permissions

Use either `drf_problems.permissions.ProblemPermissionMixin` mixin class with your existing permissions, or extend directly from `drf_problems.permissions.BaseProblemPermission`.
Define `exception_class` in the permissions to the desired exception class.
For flexibility, you can even set exception instance by setting `exception` attribute on the permission object.

Here's a sample permissions class:

```python
from drf_problems.permissions import BaseProblemPermission

class MinimumVersionRequiredPermission(BaseProblemPermission):
    exception_class = InvalidVersionRequestedException
```

### With Views

**Note**: The permissions wouldn't throw the desired exception from the view, until the view is extended from the `drf_problems.mixins.AllowPermissionWithExceptionViewMixin` mixin. So, remember to update your views too, for which permissions are updated!

## Resources

- [Official Guide](https://medium.com/@shivanshs9/drf-problems-21f7bb4d4675)
- [Problem Details for HTTP APIs](https://tools.ietf.org/html/rfc7807)
- [REST API Error Handling - Problem Details Response](https://blog.restcase.com/rest-api-error-handling-problem-details-response/)

## Roadmap

- Add tests with some sample views using exceptions and permissions.
- Document the code better.

## Contributing

Contributions are very welcome, of any kind - whether finding new issues or any ideas for enhancements or a pull request.
