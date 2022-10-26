def osztas(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if b == 0:
            raise ZeroDivisionError("Ejnye, nullával nem osztunk!")
        return a / b

    raise TypeError("Egész paramétereket adj meg!")

# === kivételkezelés ===

try:
    print(osztas(5, 2))
    print(osztas(5, 0))     # ZeroDivisionError!
    print(osztas(3, 2))
except ZeroDivisionError as zde:
    print(zde)
except TypeError as te:
    print(te)
except Exception:
    print("Valami egyéb hiba történt...")
finally:
    print("--- kivételkezelés vége ---")


class NincsPisztaciaException(Exception):
    def __init__(self, uzenet):
        self.uzenet = uzenet
        super().__init__(self.uzenet)   # ősosztály konstruktorának meghívása

try:
    fagyi_izek = ["csoki", "vanília", "szamóca", "málna", "karamell"]
    if "pisztácia" not in fagyi_izek:
        raise NincsPisztaciaException("Elfogyott a pisztácia!")
except NincsPisztaciaException as npe:
    print(npe)
