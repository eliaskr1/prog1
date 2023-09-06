import os

if os.path.exists("textfil.txt"):
    f = open("textfil.txt", "r+")
else:
    f = open("textfil.txt", "x")

f.write("Rad1\nRad2\nRad3")

f.seek(0)

text = f.read()

print(text)
