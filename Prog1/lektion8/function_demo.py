# Definiera funktion
def addera(tal1, tal2):
    summa = tal1 + tal2
    return summa


def minimum(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def greet (firstname, lastname=""):
    print("Hej " + firstname, lastname + "!")

# Anropa funktion och lagra i variabel
result = addera(1, 2)
print(result)

numbers = [3, 5, 2, 9, 6]

print(minimum(numbers))
print(numbers)

greet("Lisa", "Svensson")