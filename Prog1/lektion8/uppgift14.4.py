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
        teams[away_team]['losses'] += 1
    elif home_score < away_score:
        teams[away_team]['wins'] += 1
        teams[home_team]['losses'] += 1
    elif home_score == away_score:
        teams[away_team]['draws'] += 1
        teams[home_team]['draws'] += 1
    
# 14.5
def make_list(dict, new_key):
    """Konverterar en dictionary med nästlade dictionarys till en lista med dictionarys.
    Skapar också ett nytt element med "root" key från de nästlade dictionarys.

  Args:
    dict: Den dictionary som ska konverteras.
    new_key: ny key som får sitt value från "root" key i den nästlade dictionaryn.

  Returns:
    En lista med dictionarys.
  """
    l = []
    for key, value in dict.items():
        l.append({new_key: key, **value})
    return l 


def sort_list(list):
    # Beräkna poängen för varje nation.
    for nation in list:
        nation['points'] = nation['wins'] * 3 + nation['draws']

    # Sortera listan efter poäng, i fallande ordning.
    return sorted(list, key=lambda nation: nation['points'], reverse=True)

# 14.6
def print_table(list):
    table_width = 52
    column1 = 13
    table_num = 1
    loop = 0
    print("-"*table_width)
    print("| # | Nation        | W | D | L | GF | GA | GD | P |")
    print("-"*table_width)
    for i in list:
        nation = sorted_l[loop]['nations']
        wins = sorted_l[loop]['wins']
        draws = sorted_l[loop]['draws']
        losses = sorted_l[loop]['losses']
        gf = sorted_l[loop]['goals for']
        ga = sorted_l[loop]['goals against']
        gd = sorted_l[loop]['goals for'] - sorted_l[loop]['goals against']
        p = sorted_l[loop]['points']
        print(f"| {table_num} | {nation.ljust(column1)} | {wins} | {draws} | {losses} | {gf : > 2} | {ga : > 2} | {gd : > 2} | {p} |")
        table_num += 1
        loop += 1

add_game('Costa Rica', 0, 'Serbia', 1)
add_game('Brazil', 1, 'Switzerland', 1)

add_game('Brazil', 2, 'Costa Rica', 0)
add_game('Serbia', 1, 'Switzerland', 2)

add_game('Serbia', 0, 'Brazil', 2)
add_game('Switzerland', 2, 'Costa Rica', 2)

l = make_list(teams, 'nations')

sorted_l = sort_list(l)

print_table(sorted_l)

