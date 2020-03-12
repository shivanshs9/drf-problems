from rest_framework import exceptions, generics, response, status

from drf_problems import PROBLEM_EXCEPTION_MAP, serializers


class ErrorDocumentationView(generics.GenericAPIView):
    serializer_class = serializers.ErrorDescriptionSerializer

    @staticmethod
    def get(request, *args, **kwargs):
        error_code = kwargs['code']
        try:
            serializer = serializers.ErrorDescriptionSerializer(
                PROBLEM_EXCEPTION_MAP[error_code])
        except KeyError:
            raise exceptions.NotFound('Given error code not registered.')
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)
