import math

class Person:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress
    
    def __str__(self):
        return f"{self.name} är {self.age} år gammal och bor på {self.adress}"

p1 = Person("Elias", 25, "Birger Dahlerus väg 5")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        circ = self.radius * 2 * math.pi
        print(self, "och omkretsen", circ)
        return circ
    def __str__(self):
        return f"Cirkeln har radien {self.radius}"

c1 = Circle(3)

class BankAccount:
    def __init__(self, account_nr, balance: int):
        self.account_nr = account_nr
        self.balance = balance
    def insert(self):
        number = int(input("Input amount > "))
        self.balance += number
    def withdraw(self):
        number = int(input("Input amount> "))
        self.balance -= number
    def __str__(self):
        return f"{self.account_nr} har {self.balance} kr"
    
account = BankAccount("12345", 5324.21)


