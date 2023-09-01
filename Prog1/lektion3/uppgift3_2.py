name = input("Ange ditt namn: ")
age = int(input("ange din ålder: "))
print("--------")

if age <= 1:
    sleep = 14
elif age <= 2:
    sleep = 13
elif age <= 3:
    sleep = 12
elif age <= 4:
    sleep = 11.5
elif age <= 6:
    sleep = 11
elif age <= 7:
    sleep = 10.5
elif age <= 10:
    sleep = 10
elif age <= 11:
    sleep = 9.5
elif age <= 15:
    sleep = 9
elif age <= 16:
    sleep = 8.5
elif age >= 17:
    sleep = 8

print("Hallå", name, "! Enligt vårdguidens rekommendationer behöver individer i din ålder (", age, ") sova minst", sleep, "timmar per natt")