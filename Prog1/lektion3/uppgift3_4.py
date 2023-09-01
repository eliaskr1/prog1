n = ["DANMARK", "FINLAND", "ISLAND", "NORGE", "SVERIGE"]
b = ["ENGLAND", "SKOTTLAND", "NORDIRLAND", "WALES"]

country = input("Skriv in valfritt land: ")

x = country.upper()

if x in n:
    print("Ditt valda land ligger i Norden!")
elif x in b:
    print("Ditt valda land ligger i Storbritanien!")
else:
    print("Ditt valda land ligger varken i Norden eller i Storbritanien")
