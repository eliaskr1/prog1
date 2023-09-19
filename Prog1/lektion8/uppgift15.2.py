import random as rd
numbers = []
for x in range(10):
    numbers.append(rd.randint(0, 20))

print("BEFORE SORTING:")
for i in numbers:
    print(f"- {i}")

numbers.sort()

print("AFTER SORTING:")
for i in numbers:
    print(f"- {i}")