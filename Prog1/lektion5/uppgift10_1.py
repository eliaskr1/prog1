import os

skyltText = "Välkommen till Västerås"

print("|--------------------------------------------|")
print("|  #  ------------------------------      #  |")
print(f"| ### |{skyltText.center(28)}|  #  ### |")
print("| ### ------------------------------ ### ### |")
print("|  |        |               |         |   |  |")
print("|---------------------------------------------")
print("| C | Change sign message")
print("| E | Exit Program")
print("|------------------------")
cmd = input("|> ".lower())

if cmd == "c":
    with open ("skyltText.txt", "r+") as file:
        

elif cmd == "e":

else:
    print("Ogiltigt kommando")