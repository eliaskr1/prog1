import random as r

def get_even(list):
    even = []
    for i in list:
        if i % 2 == 0:
            even.append(i)
    return even

numbers = []

for x in range(10):
    numbers.append(r.randint(0, 9))
    
even = get_even(numbers) 

print("Even:", even)
print("Numbers:", numbers)
