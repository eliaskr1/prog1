print("Det här programmer dubblar din inmatning")
while True:
    x = input("Mata in ett heltal > ")
    try:
        x = int(x)
        break
    except ValueError:
        print(x, "är inte ett giltigt heltal")
y = x * 2
print("Resultatet är ", y, "om x är = ", x)