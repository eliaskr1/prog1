import os

POST_1 = ""
POST_2 = ""
POST_3 = ""
while True : 
    print (".: basicBILLBOARD :. ")
    print (" ******************** ")
    print ("P1:", POST_1 )
    print ("P2:", POST_2 )
    print ("P3:", POST_3 )
    print (" --------------------")
    print ("c | Ändra post ")
    print ("e | Stäng program ")
    print (" --------------------")
    cmd = input("meny > ").lower()
    if cmd == "c":
        id = input("id > ")
        if id == "1":
            POST_1 = input("meddelande > ")
        elif id == "2":
            POST_2 = input("meddelande > ")
        elif id == "3":
            POST_3 = input("meddelande > ")
        else:
            print("-FEL: Ogiltigt ID\n-INFO: Ange heltal mellan 1-3")
    elif cmd == "e":
        break
    else:
        print("-FEL: Ogiltigt kommando (", cmd,")")

    print("--------------------")
    input ("Tryck enter för att fortsätta ... ") #Paus av exe

    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")

print("--------------------")