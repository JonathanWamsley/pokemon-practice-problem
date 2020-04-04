# Pokemon problem 

'''
    You are given 2 lists:
    - pokemon_names: a list off all the known pokemon names (will refer as generic name)
    - card_names: a list of all the pokemon card names

    You recently found out that a pokemon card can have multiple pokemon in it.
    You would like to be able to show what pokemon_names (generic pokemon) are in each pokemon card. 

    Pokemon cards can include anywhere from 0, 3 generic pokemon within it. 
    Pokemon cards can also have false names inside () indicating promotion cards, etc.

    Your goal is for every pokemon card map all the generic pokemon within it
'''
import csv
import re
from itertools import zip_longest

pokemon_names = []
with open('/mnt/c/Users/jonny/programming_content/practice_programming_problems/pokemon_problem/pokemon_names.csv', 'r') as csvfile:
    csvreader  = csv.reader(csvfile, delimiter=',')
    for row in csvreader: 
        pokemon_names.append(row[0])

card_names = []
with open('/mnt/c/Users/jonny/programming_content/practice_programming_problems/pokemon_problem/card_names.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        card_names.append(row[0])

print('pokemon names head: ', pokemon_names[:5])
print('card names head: ', card_names[:5])



'''
    My solution. This was originally part of a pandas DataFrame, so I maintain the order
'''
def map_pokemon_names_to_pokemon_cards(card_names, pokemon_names):
    card_names_clean = [re.sub(r'(\(.*\))', '', card) for card in card_names] # removes the (filler card info) out of cards that may have unrelated pokemon in it
    card_names_clean_list = [card.lower().split(' ') for card in card_names_clean]
    pokemon_teams = []
    generic_name = pokemon_names # contains full name of all pokemon
    for card_name in card_names_clean_list:
        pokemon_team = set() 
        for ele1, ele2 in zip_longest(card_name[:], card_name[1:]):
            if ele1 in generic_name: # a string returns true in a list if exact match. so mr.is not in a list with ['mr. mime']
                pokemon_team.add(ele1)
            elif ele2 in generic_name:
                pokemon_team.add(ele2)
            elif str(ele1) + ' ' + str(ele2) in generic_name: # this deals with mr. mime/ mime jr. and other pokemon with 2 words combinations
                pokemon_team.add(str(ele1) + ' ' + str(ele2))
        pokemon_teams.append(pokemon_team)    
        
    for card, pokemons in zip(card_names, pokemon_teams):   
        print(f'{card}: {pokemons}')
    return pokemon_teams

pokemon_teams = map_pokemon_names_to_pokemon_cards(card_names, pokemon_names)