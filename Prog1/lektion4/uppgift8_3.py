todos = [
    "städa",
    "handla",
    "plugga",
    "ge blod"
]

print(todos)

try:
    inData = int(input("Ta bort todo (index): "))
    del todos[inData - 1]
except ValueError:
    print("FEL: Ange giltigt index. (Heltal mellan 1-4)")
except IndexError:
    print("FEL: Ange giltigt index. (Heltal mellan 1-4)")

print(todos)
