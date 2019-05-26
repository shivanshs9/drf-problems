from rest_framework.renderers import JSONRenderer


class ProblemJSONRenderer(JSONRenderer):
    """
    Renderer which serializes to JSON.
    """
    media_type = 'application/problem+json'
