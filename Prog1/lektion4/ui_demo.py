import os

ui_width = 30

while True:
    print("*" * ui_width)
    print("FÄRG-GISSAREN".center(ui_width))
    print("-" * ui_width)
    print("::REGLER::".center(ui_width))
    print("Gissa en färg".center(ui_width))
    print("Gissar du rätt färg".center(ui_width))
    print("Så vinner du spelet".center(ui_width))
    print("-" * ui_width)

    color = input("Gissa färg > ").lower()
    guesses = 1

    while color != "gul":
        print("Fel gissning, försök igen...")
        guesses += 1
        color = input("Gissa färg > ").lower()
    print("Bra jobbat, det tog dig ", guesses, "gissningar!")
    input("Tryck på retur för att spela igen")

    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")