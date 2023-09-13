import json, requests

api1 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
resp1 = requests.get(api1)
resp_dict1 = json.loads(resp1.text)
print("""
--- ARTIST DB ---
Ariana Grande
Avicii
Blink -182
Brad Paisley
Ed Sheeran
Imagine Dragons
Maroon 5
Scorpions
-----------------
Select artist:""")
cmd = input("> ")

for artist in resp_dict1['artists']:
    
