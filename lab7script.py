def main():
# Initialize the complex data structure
    hockey_team_info = {
        'name': 'Maple Leafs',
        'city': 'Toronto',
        'players': [
            'Matthews',
            'Marner',
            'Tavares'
        ],
        'games': [
            {'opponent': 'Montreal',
            'goals_for': 2,
            'goals_against': 4
            },
            {'opponent': 'Florida',
            'goals_for': 5,
            'goals_against': 2
            }
    ]
 }
   
    # Append new game to the end of the list
    new_game = {'opponent': 'Boston', 'goals_for': 9, 'goals_against': 0}
    hockey_team_info['games'].append(new_game)
   
    # Add a tuple of new players
    new_players = ('Nylander', 'Giordano', 'Campbell')
    add_players(hockey_team_info, new_players)   
    # Print list of opponents team has played games against
    print_teams_played(hockey_team_info)   

def print_teams_played(team_info):
    """
    Prints a sentence including a list of all teams played against.
   
    : param team_info: Team info data structure
    """
# Create the first part of the sentence string
    sentence = 'The '+ team_info['city'] + ' ' + team_info['name'] + ' has played games against '
   
# Iterate through every game in the data structure
    for i,g in enumerate(team_info['games']): 
# Append the city of the opponent
        sentence += g['opponent'] + ","
   
# Append appropriate punctuation
    if i < len(team_info['games']) - 1:
        sentence += ', '
    else:
        sentence += '.'
   
# Print the entire sentence
    print(sentence)
   
   
def add_players(team_info, players):
    """
       Adds tuple (or list) of players to data structure
   
       : param team_info: Team info data structure
       : param player: tuple (or list) of players to add
       """
    for p in players:
        team_info['players'].append(p)
 
main()