mTabell = int(input ("Ange en multiplikationstabell > "))
x = 1
while True:
    for i in range(x, (x+3)):
        print(mTabell * i)
        x += 1
    svar = input("Vill du fortsätta? (j/n) > ")
    if svar == "n":
        break
print("Tack")