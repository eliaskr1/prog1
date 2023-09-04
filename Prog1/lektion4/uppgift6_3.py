print("""
Palindrom eller inte?
Det här programmet undersöker om
en inmatad text är en palindrom.
--------------------------------
""")
text = input("Ange din text här > ")

tNoSpace = text.replace(" ", "")

reText = tNoSpace[::-1]

if tNoSpace == reText:
    print("Din inmatade text är en palindrom!")
else:
    print("Din inmatade text är inte en palindrom!")