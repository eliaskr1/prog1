print('''
*********************
* The Great Divider *
---------------------

Beräknar c för uttrycket:
       a / b = c
---------------------''')
while True:
    a = input("a = ")
    b = input("b = ")
    try:
        a = float(a)
        b = float(b)
        c = round(a / b, 2)
        break
    except ValueError:
        print("FEL: ", a, " eller ", b, "är inte ett giltigt tal")
    except ZeroDivisionError:
        print("FEL: du kan inte dividera med noll")
print("---------------------")
print(a, " / ", b, " = ", c)