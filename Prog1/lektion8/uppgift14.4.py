teams = {
    'Brazil' : {
    'wins' : 0,
    'draws' : 0,
    'losses' : 0,
    'goals for' : 0,
    'goals against' :0
    } ,
    'Serbia': {
    'wins': 0,
    'draws' : 0,
    'losses' : 0,
    'goals for' : 0,
    'goals against' : 0
    } ,
    'Switzerland' : {
    'wins' : 0,
    'draws' : 0,
    'losses' : 0,
    'goals for' : 0,
    'goals against' : 0
    } ,
    'Costa Rica' : {
    'wins' : 0,
    'draws' : 0,
    'losses' : 0,
    'goals for' : 0,
    'goals against' : 0
    }
}

def add_game(home_team, home_score: int, away_team, away_score: int):
    teams[home_team]['goals for'] += home_score
    teams[home_team]['goals against'] += away_score
    teams[away_team]['goals for'] += away_score
    teams[away_team]['goals against'] += home_score
    if home_score > away_score:
        teams[home_team]['wins'] += 1
    elif home_score < away_score:
        teams[away_team]['wins'] += 1
    elif home_score == away_score:
        teams[away_team]['draws'] += 1
        teams[home_team]['draws'] += 1
    
    
add_game('Costa Rica', 0, 'Serbia', 1)
add_game('Brazil', 1, 'Switzerland', 1)

add_game('Brazil', 2, 'Costa Rica', 0)
add_game('Serbia', 1, 'Switzerland', 2)

add_game('Serbia', 0, 'Brazil', 2)
add_game('Switzerland', 2, 'Costa Rica', 2)

for team in teams:
    print(teams[team])
