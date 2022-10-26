import json

adatok = dict()
adatok["nev"] = "Python Péter"
adatok["emails"] = ["hello@peti.hu", "peter.python@munkahely.hu"]
adatok["skillek"] = {"MS Word": 10, "MS Excel": 9, "Python":3, "Java":1, "C++": None}

with open("data2.json", "w") as fp:
    json.dump(adatok, fp,indent=2)