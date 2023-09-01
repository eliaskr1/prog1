celebs = [
    {
        "name" : "Daniel Radcliffe",
        "gender" : "man",
        "hair" : "brun",
        "eyes" : "brun",
    },
    {
        "name" : "Rupert Grint",
        "gender" : "man",
        "hair" : "röd",
        "eyes" : "blå",
    },
    {
        "name" : "Emma Watson",
        "gender" : "kvinna",
        "hair" : "brun",
        "eyes" : "brun",
    },
    {
        "name" : "Selena Gomez",
        "gender" : "kvinna",
        "hair" : "brun",
        "eyes" : "brun",
    },
    {
        "name" : "Tom Felton",
        "gender" : "man",
        "hair" : "blond",
        "eyes" : "blå",
    },
    {
        "name" : "Alan Rickman",
        "gender" : "man",
        "hair" : "grå",
        "eyes" : "brun",
    },
    {
        "name" : "Maggie Smith",
        "gender" : "kvinna",
        "hair" : "grå",
        "eyes" : "blå",
    },
    {
        "name" : "Evanna Lynch",
        "gender" : "kvinna",
        "hair" : "blond",
        "eyes" : "blå",
    },
    {
        "name" : "Alfred Enoch",
        "gender" : "man",
        "hair" : "brun",
        "eyes" : "brun",
    }
]

gender = input("Ange kön: ")
hair = input("Ange hårfärg: ")
eyes = input("Ange ögonfärg: ")

result = None
resultat = []
for i in celebs:
    if i["gender"] == gender and i["hair"] == hair and i["eyes"] == eyes:
        result = i["name"]
        resultat.append(result)
celebStr = " och ".join(resultat)
if result == None:
    print("Du matchar inte med några kändisar i våran databas")
else:
    print("Du matchar med ", celebStr)