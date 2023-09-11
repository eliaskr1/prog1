# Skapa dict
person = {
    "name": "Elias Kroon",
    "age": 24,
    "pets": [
        {"name": "Morris", "age": "3", "type": "hund"},
        {"name": "Lisa", "age": "2", "type": "katt"},
        {"name": "Lassi", "age": "6", "type": "hund"}
    ]
}

# Hämta element

print("Hej "+ person["name"])
print("Du är "+ str(person["age"])+ " gammal")
print(f"Du är {person['age']}  gammal")

# Referera till nycklar dynamiskt
'''
key = input("Ange nyckel > ")
try:
    print(person[key])
except KeyError:
    print("Felaktig nyckel")
'''
# Ändra element

person["age"] = 25

print(person)

# Lägg till nytt element (key-value-pair)

person["adress"] = "Birger Dahlerus väg 5"

print(person)

# Ta bort element

del(person["adress"])

print(person)

# Kopiera dict

person_copy = person.copy()
person_copy["temp"] = "temp"

print(person_copy)
print(person)

del person_copy

# Iteration av dict

for key in person:
    print(key)
    print(person[key])

# Nästlade dicts

person["adress"] = {
    "street": "Birger Dahlerus väg",
    "number": "5",
    "ort": "Järfälla",
    "postal": "17669"
}


print(person["adress"]["street"], person["adress"]["number"])
print(person["adress"]["ort"].upper(), person["adress"]["postal"])

namn = person["name"]
age = person["age"]
pets = person["pets"]
count_pets = len(pets)

print(f"*{namn} är {age} år gammal och har {count_pets} husdjur.")
for pet in pets:
    print(f"* En {pet['age']} år gammal {pet['type']} som heter {pet['name']}")
