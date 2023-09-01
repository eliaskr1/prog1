import math
# Uppgift 2.1
"""
citat = "datatyper har inbyggda metoder"
print (citat.upper())
"""

# Uppgift 2.2
"""
flytTal = float(input("ange ditt flyttal: "))
print ("avrundat flyttal = ", round(flytTal))
"""

# Uppgift 2.3
""""
print("Hallå!")
firstName = input("Vad är ditt förnamn? ")
lastName = input("Vad är ditt efternamn? ")
print("Trevligt att träffas", firstName, lastName, "!")
"""
#uppgift 2.4
"""
age = int(input("Hur gammal är du? "))

if age >= 18:
    print("Du är myndig, grattis!")
else:
    print("Du är myndig inom ", 18 - age, " år")
"""
#uppgift 2.5
"""
a = int(input ("Mata in heltal #1: "))
b = int(input ("Mata in heltal #2: "))
c = int(input ("Mata in heltal #3: "))
d = int(input ("Mata in heltal #4: "))
e = int(input ("Mata in heltal #5: "))

print("Det högsta inmatade heltalet är: ", max(a, b, c, d, e))

"""
#uppgift 2.6
print(" . : KORVKOLLEN : .  ")
print("_____________________")

vanligKorv2 = int(input("Hur många elever vill ha 2 vanliga korvar? "))
vanligKorv3 = int(input("Hur många elever vill ha 3 vanliga korvar? "))
vegoKorv2 = int(input("Hur många elever vill ha 2 veganska korvar? "))
vegoKorv3 = int(input("Hur många elever vill ha 3 veganska korvar? "))
vanligKorv = vanligKorv2 * 2 + vanligKorv3 * 3
vegoKorv = vegoKorv2 * 2 + vegoKorv3 * 3
elever = vanligKorv2 + vanligKorv3 + vegoKorv2 + vegoKorv3

print("_____________________")
print(" . : INKÖPSLISTA : . ")
print("_____________________")

korvPaket = vanligKorv / 8
vegoKorvPaket = vegoKorv / 4
prisVanligKorv = math.ceil(korvPaket) * 20.95
prisVegoKorv = math.ceil(vegoKorvPaket) * 34.95
prisDricka = elever * 13.95

print("| Vanlig korv:  ", math.ceil(korvPaket), " förpackningar")
print("| Vegansk korv: ", math.ceil(vegoKorvPaket), " förpackningar")
print("| Dricka:       ", elever, " drickor")
print("____________________")
print(round(prisVanligKorv + prisVegoKorv + prisDricka, 1), " SEK")
print("____________________")