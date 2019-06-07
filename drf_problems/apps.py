from django.apps import AppConfig
from rest_framework import exceptions as drf_exceptions

from drf_problems.utils import register_exception


class DrfProblemsConfig(AppConfig):
    name = 'drf_problems'

    def ready(self):
        register_exception(drf_exceptions.APIException)
        register_exception(drf_exceptions.ValidationError)
        register_exception(drf_exceptions.ParseError)
        register_exception(drf_exceptions.AuthenticationFailed)
        register_exception(drf_exceptions.NotAuthenticated)
        register_exception(drf_exceptions.PermissionDenied)
        register_exception(drf_exceptions.NotFound)
        register_exception(drf_exceptions.MethodNotAllowed)
        register_exception(drf_exceptions.NotAcceptable)
        register_exception(drf_exceptions.UnsupportedMediaType)
        register_exception(drf_exceptions.Throttled)
