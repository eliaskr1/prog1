import csv
import os
# Funktion för att läsa igenom CSV filen
def load_csv(filename):
    data = []
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file) # DictReader läser in data från en CSV fil till en dict där keys tas från översta rader i csv filen
        for row in reader:
            data.append(row)
    return data
# Sparar filvägen i en variabel
csv_file = "database.csv"

while True:
    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    try:
        # Printa menyn med kommandon
        print(".: PEOPLES DATABASE :.")
        print("----------------------")
        print("get_id | Get person by ID")
        print("scan_f | List people by FORENAME")
        print("scan_s | List people by SURNAME")
        print("exit   | Exit program")
        print("----------------------")
        cmd = input("| > ").lower()
        if cmd == "get_id":
            print("----------------------")
            id = int(input("ID > "))
            data = load_csv(csv_file)
            found = False
            for person in data:
                if int(person["ID"]) == id:
                    print("----------------------")
                    print(f"ID: {person['ID']}")
                    print(f"FORENAME: {person['FORENAME']}")
                    print(f"SURNAME: {person['SURNAME']}")
                    print(f"GENDER: {person['GENDER']}")
                    print(f"YEAR: {person['YEAR']}")
                    found = True
                    break
        # Sök förnamn
        elif cmd == "scan_f":
            print("----------------------")
            fName = input("FORENAME > ")
            data = load_csv(csv_file)
            found = False
            for person in data:
                if person['FORENAME'].lower() == fName.lower():
                    print("----------------------")
                    print(f"{person['ID']}, {person['FORENAME']}, {person['SURNAME']}, {person['GENDER']}, {person['YEAR']}")
                    found = True                    
            if not found:
                print("No matching persons found.")
        # Sök efternamn
        elif cmd == "scan_s":
            print("----------------------")
            sName = input("SURNAME > ")
            data = load_csv(csv_file)
            found = False
            for person in data:
                if person['SURNAME'].lower() == sName.lower():
                    print("----------------------")
                    print(f"{person['ID']}, {person['FORENAME']}, {person['SURNAME']}, {person['GENDER']}, {person['YEAR']}")
                    found = True
            if not found:
                print("No matching persons found.")
        elif cmd ==("exit"):
            break
        else:
            print("----------------------")
            print("ERROR: Invalid command")
    except ValueError:
        print("ERROR: ID has to be an integer")
    input("Press 'Enter' to go again")