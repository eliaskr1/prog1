import random
dice = random.randint(1, 6)

d1 = '''
---------
|       |
|   x   |
|       |
---------
'''
d2 = '''
---------
| x     |
|       |
|     x |
---------
'''
d3 = '''
---------
| x     |
|   x   |
|     x |
---------
'''
d4 = '''
---------
| x   x |
|       |
| x   x |
---------
'''
d5 = '''
---------
| x   x |
|   x   |
| x   x |
---------
'''
d6 = '''
---------
| x   x |
| x   x |
| x   x |
---------
'''
print("Du slog en ", dice, ":a!")
if dice == 1:
    print(d1)
elif dice == 2:
    print(d2)
elif dice == 3:
    print(d3)
elif dice == 4:
    print(d4)
elif dice == 5:
    print(d5)
elif dice == 6:
    print(d6)