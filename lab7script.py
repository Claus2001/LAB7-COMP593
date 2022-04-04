def main():
# Initialize the complex data structure
    my_info = {
        'name': 'Claus de la Guardia',
        'student_id': '1234567890',
        'pizza_toppings': [
            'Bacon',
            'Onion',
            'Feta Chesse'
        ],
        'movies': [
            {'genre': 'Sci-fi',
            'goals_for': 2,
            'goals_against': 4
            },
            {'genre': 'Comedy',
            'The hangover' : 1,
            'goals_against': 2
            }
    ]
 }
   
    # Append new game to the end of the list
    #new_movie = {'opponent': 'Boston', 'goals_for': 9, 'goals_against': 0}
    #my_info['games'].append(new_game)
   
    # Add a tuple of new players
    new_players = ('Nylander', 'Giordano', 'Campbell')
    add_players(my_info, new_players)   
    # Print list of opponents team has played games against
    print_teams_played(my_info)   

def print_teams_played(all_info):
    """
    Prints a sentence including a list of all teams played against.
   
    : param team_info: Team info data structure
    """
# Create the first part of the sentence string
    sentence = 'Hi jeremy, my name is '+ all_info['name'] + 'and my studend ID is ' + all_info['student_id'] + ' my ideal pizza has' + all_info['pizza_toppings']
    print(sentence)
# Iterate through every game in the data structure
    for i,g in enumerate(all_info['games']): 
# Append the city of the opponent
        sentence += g['opponent'] + ","
   
# Append appropriate punctuation
    if i < len(all_info['games']) - 1:
        sentence += ', '
    else:
        sentence += '.'
   
# Print the entire sentence
    print(sentence)
   
   
def add_players(all_info, players):
    """
       Adds tuple (or list) of players to data structure
   
       : param team_info: Team info data structure
       : param player: tuple (or list) of players to add
       """
    for p in players:
        all_info['players'].append(p)
 
main()