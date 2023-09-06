registrerade =[" Anna ", " Eva ", " Erik ", " Lars ", " Karl "]
avanmälningar =[" Anna ", " Erik ", " Karl "]

for i in registrerade:
    if i in avanmälningar:
        registrerade.remove(i)

for i in registrerade:
    print(i)