MAX_NUM = 1000

def addera(tal1, tal2):
    summa = tal1 + tal2
    return summa


def minimum(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def greet (firstname, lastname=""):
    print("Hej " + firstname, lastname + "!")