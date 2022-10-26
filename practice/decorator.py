def elso_dekorator(func):
    def wrapper():
        print("Hamarosan meghivjuk a fuggvenyt.")
        func()
        print("Fuggveny befejezve.")
    return wrapper

def greetings():
    print("Hello there!")

greetings = elso_dekorator(greetings)

greetings()
