import json

szinek = []

with open ("data.json","r") as fp:
    szinek = json.load(fp)
    szinek = szinek["colors"]

for szin in szinek:
    print(szin["color"])


hex = [szin["code"].get("hex") for szin in szinek]
print(hex)