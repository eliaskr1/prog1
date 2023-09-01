tal1 = int(input("Ange ett heltal "))
tal2 = int(input("Ange ett till heltal "))
tal3 = int(input("Ange ännu ett heltal "))

if tal1 > tal2:
    if tal1 > tal3:
        print(tal1, "är det största talet.")
    else:
        print(tal3, "är det största talet.")
elif tal2 > tal3:
    print(tal2, "är det största talet")
else:
    print(tal3, "är det största talet")