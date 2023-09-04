import os

if os.name == ("nt"):
    os.system("cls")
    print("Du kör windows")
elif os.name == posix:
    os.system("clear")
    print("Du kör mac eller linux")
