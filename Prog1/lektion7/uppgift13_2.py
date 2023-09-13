import requests, json

print('''Enter the name of which of the 
following cities you want weather forcasts for
    • Stockholm
    • Göteborg
    • Malmö
    • Uppsala
    • Västerås''')
city = input("> ")
city = city.replace("å", "a")
city = city.replace("ä", "a")
city = city.replace("ö", "o")

url = "https://54qhf521ze.execute-api.eu-north-1.amazonaws.com/weather/"+ city

resp = requests.get(url).text
resp_dict = json.loads(resp)

print("---------------------")
print("      FORECASTS      ")
print("*********************")
try:
    for forecast in resp_dict["forecasts"]:
        print(forecast['date'],"     ", forecast['forecast'])
except KeyError:
    print("Ogiltig stad angiven.")