from drf_problems import PROBLEM_DESCRIPTION_MAP


def register_exception(exc_cls):
    PROBLEM_DESCRIPTION_MAP[exc_cls.default_code] = exc_cls.description
