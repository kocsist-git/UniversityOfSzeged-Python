class Celsius:
    def __init__(self, homerseklet=0):
        self._homerseklet = homerseklet

    @property
    def homerseklet(self):
        print("Lekerjuk")
        return self._homerseklet

    @homerseklet.setter
    def homerseklet(self, value):
        if value < -273:
            print("Nem lehet -273 foknal hidegebbet beallitani")
        else:
            print("Beallitjuk")
            self._homerseklet = value


c1 = Celsius(30)
c1.homerseklet = 100
print(c1.homerseklet)
