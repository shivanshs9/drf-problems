from rest_framework.reverse import reverse
from rest_framework.views import exception_handler as drf_exception_handler


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    response.content_type = 'application/problem+json'
    data = response.data

    problem_title = getattr(exc, 'title', response.status_text)
    problem_status = response.status_code
    problem_code = getattr(exc, 'default_code', 'error')
    problem_type = reverse('drf_problems:error-documentation',
                           kwargs={'code': problem_code}, request=context['request'])
    if isinstance(data, dict):
        data['title'] = problem_title
        data['status'] = problem_status
        data['type'] = problem_type
    else:
        data = dict(errors=response.data, title=problem_title,
                    status=problem_status, type=problem_type)
    response.data = data

    return response
