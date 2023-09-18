import json, requests
# Hämta data från första APIn för att kunna få ut ID
api1 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"
resp1 = requests.get(api1)
resp_dict1 = json.loads(resp1.text)
print("""
--- ARTIST DB ---
Ariana Grande
Avicii
Blink-182
Brad Paisley
Ed Sheeran
Imagine Dragons
Maroon 5
Scorpions
-----------------
Select artist:""")
cmd = input("> ")

# Söker igenom API1 för att hitta ID till angiven artist
found = False

for artist in resp_dict1['artists']:
    if artist['name'] == cmd:
        api2 = "https://5hyqtreww2.execute-api.eu-north-1.amazonaws.com/artists/"+ artist['id']
        resp2 = requests.get(api2)
        resp_dict2 = json.loads(resp2.text)
        found = True


# Skapar snyggare strängar att skriva ut
try:
    active = resp_dict2['artist']['years_active']
    active = ", ".join(active)
    members = resp_dict2['artist']['members']
    members = ", ".join(members)
    genres = resp_dict2['artist']['genres']
    genres = ", ".join(genres)

    print("-----------------")
    print(cmd)
    print("*****************")
    print("Genres:", genres)
    print("Years active:", active)
    print("Members:", members)
    print("-----------------")

except NameError:
    print(cmd, "är inte en giltig artist.")
