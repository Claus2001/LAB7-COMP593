from turtle import title


def main():
# Initialize the complex data structure
    my_info = {
        'name': 'Claus de la Guardia',
        'student_id': 10228127,
        'pizza_toppings': [
            'Bacon',
            'Onion',
            'Feta'
        ],
        'movies': [
            {'title': 'Star Wars',
            'genre': 'Sci-fi' ,
            },
            {'title': 'The Hangover',
            'genre': 'Comedy'
            }
        ]
     }
   
    # Append new game to the end of the list
    new_movie = {'title': 'Batman', 'genre': 'Action'}
    my_info['movies'].append(new_movie)
   
    # Add a tuple of new players
    new_toppings = ('BBQ', 'Chicken', 'Jalapeño')
    add_pizza_tops(my_info, new_toppings)   
    # Print list of opponents team has played games against
    print_my_info(my_info)   

def add_pizza_tops(all_info, pizza):
    """
       Adds tuple (or list) of players to data structure
   
       : param team_info: Team info data structure
       : param player: tuple (or list) of players to add
       """
    for p in pizza:
        all_info['pizza_toppings'].append(p)

def print_my_info(all_info):
    """
    Prints a sentence including a list of all teams played against.
   
    : param team_info: Team info data structure
    """
# Create the first sentence
    my_name = all_info['name']
    id_num = all_info['student_id']

    print('Hey Jeremy, my name is ' + my_name + " and my student ID is " + str(id_num) + "." )

#Creates second sentence about pizzas with list
    toppings = []
    for n in all_info['pizza_toppings']:
        toppings.append(n)
    print('My ideal pizza has', toppings[0], toppings[1], toppings[2], toppings[-1], toppings[-2] )

#Creates third senetence about movie titles and genres using list
    mov_genre = []
    for n in all_info['movies']:
        genre = n['title']
        mov_genre.append(genre)
    print("I like to watch", mov_genre[0], mov_genre[1], mov_genre[2], "movies.")

    mov_name = []
    for n in all_info['movies']:
        title = n['title']
        mov_name.append(title)
    print('Some of my favorites are', mov_name[0], mov_name[1], mov_name[2])
   

    

 
main()