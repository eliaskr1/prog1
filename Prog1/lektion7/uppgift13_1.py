import requests, json


try:
    heltal = input("Ange positivt heltal: ")
    url = "https://4bbh01oqwj.execute-api.eu-north-1.amazonaws.com/numcheck?integer=" + heltal
    heltal_int = int(heltal)
    if heltal_int > 0:
        response = requests.get(url)
        resp_dict = json.loads(response.text)
        f = []
        for factor in resp_dict['factors']:
            f.append(factor)
        x = str(f)
        y = x.strip("[]")
        if resp_dict['even'] == True:
            even_str = heltal + " är ett jämnt nummer."
        else:
            even_str = heltal + " är inte ett jämnt nummer."
        if resp_dict['prime'] == True:
            prime_str = "Numret är ett primtal."
        else:
            prime_str = "Numret är inte ett primtal."
        
        print(even_str, prime_str)
        print(f"Numrets faktorer är", y)
    else:
        print(heltal, "är inte ett positivt heltal")
except ValueError:
    print("FEL! Inmatad data är inte ett heltal.")
