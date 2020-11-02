from drf_problems import PROBLEM_CODE_CHOICES, PROBLEM_EXCEPTION_MAP


def register_exception(exc_cls):
    code = getattr(exc_cls, 'code', exc_cls.default_code)
    PROBLEM_EXCEPTION_MAP[code] = exc_cls
    PROBLEM_CODE_CHOICES.append((code, code))


class register(object):
    def __new__(cls, target_cls):
        register_exception(target_cls)
        return target_cls
