from rest_framework import generics, response, status

from drf_problems import PROBLEM_DESCRIPTION_MAP


class ErrorDocumentationView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        error_code = kwargs['code']
        data = {
            'code': error_code,
            'description': PROBLEM_DESCRIPTION_MAP.get(error_code, 'Not provided.')
        }
        return response.Response(data=data, status=status.HTTP_200_OK)
