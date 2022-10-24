
try:
    pass
    # a kód azon része, ahol kivetel dobodhat
except ExceptionType as exc:
    pass
    # ExceptionType hiba kezelése 
except ExceptionType2 as exc:
    pass
    # ExceptionType2 hiba kezelése
else:
    pass
    # ha nem erkezett kivetel, akkor lefut 
finally:
    pass
    # mindenkeppen lefut

# Sajat kivetel osztaly is keszitheto

class BadCharacterName(Exception):
    def __init__(self, bad_name):
        self.bad_name = bad_name

try:
    raise BadCharacterName("A")
except BadCharacterName as bcn:
    print(bcn.bad_name, 'is not a valid name.')
