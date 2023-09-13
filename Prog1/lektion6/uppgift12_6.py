import os, json

with open('notes.json') as f:
    notes = json.loads(f.read())

while True:
    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print('''
.: ALWAYSNOTE :.
-- GOLD EDITION --
------------------''')
    for key in notes:
        print("-", key)
    print('''-----------------
view | view note
add  | add/change note
rm   | remove note
exit | exit program
-------------------''')
    try:
        cmd = input("menu > ").lower()
        if cmd == "add":
            print("Lägg till artikel: ")
            in_data = input("Titel: ")
            in_data2 = input("Text: ")
            notes[in_data] = in_data2
        elif cmd == "view":
            titel = input("Titel > ")
            print(notes[titel])
            input("Tryck retur för att köra igen...")
        elif cmd == "rm":
            print("Ta bort artikel: ")
            rm_data = input("Titel: ")
            del notes[rm_data]
        elif cmd == "exit":
            with open('notes.json', 'w') as file:
                file.write(json.dumps(notes))
            break
        else:
            print("FEL! Ogiltigt kommando")
            input("Tryck på retur för att försöka igen...")
    except KeyError:
        print("FEL! Ogiltig key. Keys finns i listan med anteckningar.")
        input("Tryck på retur för att försöka igen...")