import csv
counters = [0] * 10

with open("numbers.csv") as file:
    csv_reader = csv.reader(file)
    for data in csv_reader:
        for digit_str in data: # Extra for loop cuz går inte att omvandla lista till int
            digit = int(digit_str)
            counters[digit] += 1

print("---------------")
print("- NUMANALYZER -")
print("---------------")
for digit in range(10):
    print(f"| {digit} | {counters[digit]}")