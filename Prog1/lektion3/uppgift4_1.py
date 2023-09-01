talserie = []
tal = 1
while tal >= 0:
    tal = int(input("Ange ett heltal > "))
    talserie.append(tal)
talserie.pop()
print("---------------------")
print("Lägsta angivna tal = ", min(talserie))
print("Högsta angivna tal = ", max(talserie))
print("Summan av angivna tal = ", sum(talserie))
print("Medelvärdet av angivna tal = ", sum(talserie) / len(talserie))