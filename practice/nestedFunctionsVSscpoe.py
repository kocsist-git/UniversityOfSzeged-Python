x = 0


def kulso():
    x = 1

    def belso():
        x = 2
        print("belso:", x)
    belso()
    print("kulso:", x)


kulso()
print("global:", x)

###

x = 0


def kulso():
    x = 1

    def belso():
        nonlocal x # nonlocal használata
        x= 2 
        print("belso:", x)
    belso()
    print("kulso:", x)


kulso()
print("global:", x)


###

x = 0


def kulso():
    x = 1

    def belso():
        global x # global használata
        x= 2 
        print("belso:", x)
    belso()
    print("kulso:", x)


kulso()
print("global:", x)
