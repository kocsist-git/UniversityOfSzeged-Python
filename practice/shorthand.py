from re import A


kor = int(input("Kor:"))
kor_str = "fiatal" if kor < 18 else "felnott"

kor_str = "gyerek" if kor < 13 else "fiatal" if kor < 18 else "felnott"

def get_name():
    feltetel = True
    return "Almas Pite" if feltetel else None

name = get_name() or "Anonymous"