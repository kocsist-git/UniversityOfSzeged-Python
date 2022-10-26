import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        eltelt_ido = end-start
        print(f"Eltelt ido: {eltelt_ido:0.4f} masodperc")
        return value
    return wrapper_decorator


@timer
def akarmi():
    import time
    time.sleep(1)
    return dict(nev="Micimacko", kedvence="mez")

print(akarmi())