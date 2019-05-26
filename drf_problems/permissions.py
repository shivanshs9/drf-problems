from distutils.version import StrictVersion

from django.utils import six
from rest_framework import VERSION
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission

from drf_problems import exceptions

try:
    from rest_framework.permissions import BasePermissionMetaclass
except ImportError:
    class BasePermissionMetaclass(type):
        pass


def _has_composable_permissions():
    return StrictVersion(VERSION) >= '3.9.0'


class ProblemPermissionMixin(object):
    exception_class = PermissionDenied

    def __call__(self):
        return self

    def get_exception_class(self):
        return self.exception_class

    def get_exception(self):
        return getattr(self, 'exception', self.get_exception_class()())


if _has_composable_permissions():  # noqa
    from rest_framework.permissions import AND as DRF_AND
    from rest_framework.permissions import OR as DRF_OR
    from rest_framework.permissions import OperandHolder

    class AND(ProblemPermissionMixin, DRF_AND):
        def set_exception(self, result1, result2):
            if not result1:
                self.exception = self.op1.get_exception()
            elif not result2:
                self.exception = self.op2.get_exception()

        def has_permission(self, request, view):
            result1 = self.op1.has_permission(request, view)
            result2 = self.op2.has_permission(request, view)
            self.set_exception(result1, result2)
            return result1 & result2

        def has_object_permission(self, request, view, obj):
            result1 = self.op1.has_object_permission(request, view, obj)
            result2 = self.op2.has_object_permission(request, view, obj)
            self.set_exception(result1, result2)
            return result1 & result2

    class OR(ProblemPermissionMixin, DRF_OR):
        def set_exception(self, result1, result2):
            if not result1:
                self.exception = self.op1.get_exception()

        def has_permission(self, request, view):
            result1 = self.op1.has_permission(request, view)
            result2 = self.op2.has_permission(request, view)
            self.set_exception(result1, result2)
            return result1 | result2

        def has_object_permission(self, request, view, obj):
            result1 = self.op1.has_object_permission(request, view, obj)
            result2 = self.op2.has_object_permission(request, view, obj)
            self.set_exception(result1, result2)
            return result1 | result2


class BaseProblemPermissionMetaclass(BasePermissionMetaclass):
    if _has_composable_permissions():
        def __and__(cls, other):
            return OperandHolder(AND, cls, other)

        def __or__(cls, other):
            return OperandHolder(OR, cls, other)

        def __rand__(cls, other):
            return OperandHolder(AND, other, cls)

        def __ror__(cls, other):
            return OperandHolder(OR, other, cls)


@six.add_metaclass(BaseProblemPermissionMetaclass)
class BaseProblemPermission(ProblemPermissionMixin, BasePermission):
    pass


class MinimumVersionRequiredPermission(BaseProblemPermission):
    def __init__(self, min_version, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_version = StrictVersion(min_version)

    def has_permission(self, request, view):
        try:
            self.exception = exceptions.DeprecatedVersionUsedException(
                request.version, self.min_version)
            return request.version >= self.min_version
        except ValueError:
            self.exception = exceptions.InvalidVersionRequestedException(
                request.version)
        return False
