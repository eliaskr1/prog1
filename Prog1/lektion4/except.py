x = input("mata in ett heltal: ")

try:
    y = int(x)
    print(y * 2)
except ValueError:
    print(x, "är inte ett giltigt heltal")
