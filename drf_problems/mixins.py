class AllowPermissionWithExceptionViewMixin(object):
    """This is a DRF view mixin, which overrides how exceptions are raised when
    permission check fails.
    Make sure to use 'drf_problems.permissions.ProblemPermissionMixin' with your
    permission classes.

    Raises:
        exc -- Exception provided by the failed permission.
    """

    @staticmethod
    def raise_permission_error(exc):
        raise exc

    def check_permissions(self, request):
        """
        Check if the request should be permitted.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            if not permission.has_permission(request, self):
                try:
                    self.raise_permission_error(permission.get_exception())
                except AttributeError:
                    self.permission_denied(
                        request, message=getattr(permission, 'message', None)
                    )

    def check_object_permissions(self, request, obj):
        """Check if the request should be permitted for a given object.
        Raises an appropriate exception if the request is not permitted.
        """
        for permission in self.get_permissions():
            if not permission.has_object_permission(request, self, obj):
                try:
                    self.raise_permission_error(permission.get_exception())
                except AttributeError:
                    self.permission_denied(
                        request, message=getattr(permission, 'message', None)
                    )
