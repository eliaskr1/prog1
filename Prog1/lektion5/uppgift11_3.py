import json, os

# Funktion för att ladda tidigare data från filen eller returnera en tom lista om filen är tom eller saknas.
def load_intList():
    try:
        with open('intFile.json', 'r') as f:
            # Läser data från fil till list variabel
            intList = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        intList = []
    return intList

intList = load_intList()

while True:
    if os.name == "nt": # Rensa terminal
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")   
    try:
        print(".: intMEMORIZER :.")
        print("******************")
        for row in intList:
            print("* ", row)
        print("------------------")
        print(f"SUMMA : {sum(intList)}")
        print("------------------")
        print("mata in heltal")
        print("0 stänger scriptet")
        print("T tömmer listan på data")
        print("------------------")
        cmd = input("> ").lower()
        if cmd == "t":
            intList = []
            with open('intFile.json', 'w') as f:
                json.dump(intList, f)
        elif int(cmd) == 0:
            break
        else:
            # Lägg till angivet heltal i listan.
            intList.append(int(cmd))
            # Skriv listan till JSON filen
            with open('intFile.json', 'w') as f:
                json.dump(intList, f)
    # Om använder matar in en sträng som inte kan omvandlas till heltal fångas exception här    
    except ValueError:
        
        print(cmd, " är inte ett giltigt heltal")
        input("Tryck på retur för att fortsätta.")
