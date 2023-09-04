print("Det här programmet räknar instanser av \nen specifierad bokstav i en specifierad text.")
text = input("Ange din text >").lower()
char = input("Ange bokstav som ska räknas >").lower()

times = 0
index = 0

while index < len(text):
    if text[index] == char:
        times += 1
    index += 1

print("Bokstaven ", char, " förekommer i texten ", times, "gånger")