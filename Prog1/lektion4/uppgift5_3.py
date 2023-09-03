print('''
.:    MATHLETE   :.
Mata in heltal så länge du vill.
Mata in exit när du inte orkar längre.
-------------------
''')
l = []
n = None
while n != "exit":
    n = input("> ").lower()
    try:
        l.append(int(n))
    except ValueError:
        if n == "exit":
            break
        print("FEL: Ogiltigt nummer")
print("-------------------")
print("Kardinalitet: ", len(l))
print("Summa:        ", sum(l))
print("Medelvärde:   ", sum(l) / len(l))