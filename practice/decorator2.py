import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # A hivas elott tortenhet vmi.
        value=func (*args, **kwargs)
        # A hivas utan törtenhet valami
        return value
    return wrapper_decorator
