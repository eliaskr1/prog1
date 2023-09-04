todos = [
    "städa",
    "handla",
    "plugga",
    "ge blod"
]

print(todos)

inData = input("Ange todo: ")

if inData in todos:
    print("'",inData,"'", " finns redan med i listan")
else:
    print(inData, " finns inte med i listan")
    cmd = input("Vill du lägga till denna todo? (j/n)")
    if cmd == "j":
        todos.append(inData)
        print("Todo tillagd!")
    else:   
        print("Uppgiften las inte till i listan")

print(todos)
