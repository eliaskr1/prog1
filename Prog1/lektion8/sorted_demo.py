fotboll = [
    {'country': 'Russia', 'points': 3},
    {'country': 'Brazil', 'points': 7},
    {'country': 'Cameroon', 'points': 1},
    {'country': 'Sweden', 'points': 5}
]

def get_points(element):
    return element['points']

fotboll = sorted(fotboll, key=get_points, reverse=True)
fotboll.sort(key=get_points, reverse=True)

print(fotboll)
