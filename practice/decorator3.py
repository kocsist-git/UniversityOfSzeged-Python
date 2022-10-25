import functools
import json


def serialize(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        value = func(*args, **kwargs)
        # return str(value)
        value = json.dumps(value)
        return value
    return wrapper_decorator

@serialize
def akarmi():
    return dict(nev="Micimacko", kedvence="mez")