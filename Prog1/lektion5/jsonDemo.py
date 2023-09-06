import json
attendants = ['Åsa', 'Kalle', 'Olivia', 'Johan']
with open('data.json', 'w') as f:
    f.write(json.dumps(attendants))