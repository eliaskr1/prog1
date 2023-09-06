import os
ui_width = 30

stack = ["Mercedes", "Volvo", "Toyota"]

while True:
    num = 1
    try:
        print(".: STACKMASTER :.".center(ui_width))
        print("-"*ui_width)
        for i in stack:
            print(num, "- ", i)
            num += 1
        print("-"*ui_width)
        print("| MENU |".center(ui_width))
        print("push | Push element to stack")
        print("pull | Pull element from stack")
        print("exit | Exit program")
        print("-"*ui_width)

        cmd = input("MENU > ".lower())

        if cmd == "push":
            n = input("Ange bilmärke du vill addera > ")
            stack.append(n)
        elif cmd == "pull":
            i = int(input("Ange ID du vill ta bort > "))
            stack.pop(i - 1)
        elif cmd == "exit":
            break
        else:
            print(cmd, " är inte ett giltigt kommando")
            input("Tryck retur för att köra igen...")
        if os.name == "nt": # Rensa terminal
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
    except ValueError:
        print(i, " är inte ett giltigt heltal")
        if os.name == "nt": # Rensa terminal
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
    except IndexError:
        print(i, " är inte ett giltigt ID")
        if os.name == "nt": # Rensa terminal
            os.system("cls")
        elif os.name == "posix":
            os.system("clear")
    
            