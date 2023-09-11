notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg!": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}
print('''
ANTECKNINGAR:
-------------''')

for key in notes:
    print("Titel:", key)
    print("Text:", notes[key])
    print("--------------")

titel = input("Anteckning > ")
try:
    print(notes[titel])
except KeyError:
    print("Inte giltig anteckning.")