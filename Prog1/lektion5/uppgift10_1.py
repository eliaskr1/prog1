import os

while True:
    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    if os.path.exists("skyltText.txt"):
        with open ("skyltText.txt", "r") as file: # "r" för att läsa in text och printa i skylten
            filText = file.read()
            print("|--------------------------------------------|")
            print("|  #  ------------------------------      #  |")
            print(f"| ### |{filText.center(28)}|  #  ### |") # Vad vet ni om mina skyltar?????
            print("| ### ------------------------------ ### ### |")
            print("|  |        |               |         |   |  |")
            print("|---------------------------------------------")
            print("| C | Change sign message")
            print("| E | Exit Program")
            print("|------------------------")
        cmd = input("|> ".lower())
        if cmd == "c":
            with open ("skyltText.txt", "w") as file: # "w" för att skriva in ny skylttext
                nySkylt = input("|New sign message> ")
                file.write(nySkylt)
        elif cmd == "e":
            break
        else:
            print("Ogiltigt kommando")
    else:
        open("skyltText.txt", "x")
        