def km_to_miles(dist):
    if "km" in dist:
        dist = dist.strip(" km")
        int_dist = int(dist)
        print(int_dist, "km motsvarar", int_dist*0.62, "miles")
def miles_to_km(dist):
    if "miles" in dist:
        dist = dist.strip(" miles")
        int_dist = int(dist)
        print(int_dist, "miles motsvarar", int_dist*1.61, "km")

in_data = input("Ange distans > ").lower()

if "km" in in_data:
    km_to_miles(in_data)
elif "miles" in in_data:
    miles_to_km(in_data)
else:
    print("Vänligen ange giltig input")


