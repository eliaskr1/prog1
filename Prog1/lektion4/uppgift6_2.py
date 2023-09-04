const = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
robberText = ""

print("""
ROBBER TRANSLATE
----------------
""")

text = input("Svenska   <")

for i in text:
    if i in const:
        robberText += i
        robberText += "o"
        robberText += i
    else:
        robberText += i
        
print(robberText)
