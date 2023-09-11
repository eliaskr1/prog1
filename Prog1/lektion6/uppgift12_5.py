import os
notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg!": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"
}

while True:
    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    for key in notes:
        print("Titel:", key)
        print("Text:", notes[key])
        print("--------------")

    print("Ta bort artikel: ")
    cmd = input("Titel: ")

    del notes[cmd]
