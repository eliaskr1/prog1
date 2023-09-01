import random
n = random.randint(0, 100)
print(".: THE HIGHER LOWER GAME :.")
print("---------------------------")
print("Welcome to the Higher Lower")
print("Game. I  will  randomize  a")
print("number  between  0  and  99")
print("Can you guess  the  number?")
guess = -1
x = 0
while guess != n:
    guess = int(input("Your guess > "))
    if guess > n:
        print("LOWER!")
        x += 1
    elif guess < n:
        x += 1
        print("HIGHER!")
x += 1
print(guess, "IS CORRECT!")
print("It took you ", x, " guesses!")