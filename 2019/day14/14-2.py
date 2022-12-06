'''
DAY 14-2: How much FUEL can we create?

This is a rare instance where the code from 14-1 will essentially work as-is for
part 2. We can just expand our wishlist by the number of FUEL units that we want,
and then see how much ORE that will require.

From there we just create a crude search mechanism (binary or others would be faster)
to find the point at which creating an extra unit of FUEL is no longer possible
''' 
import re
from collections import defaultdict
import pprint
import math

def main():
    with open('day14/14-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    reaction_data = input_data.split('\n')

    reactions = create_reaction_dict(reaction_data)
    available_ore = 1000000000000
    fuel_units = 1

    while try_create(reactions, fuel_units, available_ore) == True:
        fuel_units *= 2
    
    upper_bound = fuel_units
    lower_bound = fuel_units / 2

    while try_create(reactions, lower_bound, available_ore) == True:
        lower_bound += 1000
    
    lower_bound -= 1000

    while try_create(reactions, lower_bound, available_ore) == True:
        lower_bound += 1

    print('Final answer: ', int(lower_bound - 1))


def create_reaction_dict(reaction_data):
    reactions = {}
    for r in reaction_data:
        output = r.split(' => ')[1].split(' ')[1]
        quantity = int(r.split(' => ')[1].split(' ')[0])
        ingredients = re.findall(r'[0-9]+\ [A-Z]+', r.split(' => ')[0])
        i_dict = {}
        for i in ingredients:
            i_dict[i.split(' ')[1]] = int(i.split(' ')[0])

        r_dict = {'quantity': quantity, 'ingredients': i_dict}
        reactions[output] = r_dict
    
    return reactions


def try_create(reactions, quantity, available = 1000000000000):
    leftovers = defaultdict(int)
    wishlist = defaultdict(int)
    ore_required = 0

    for key in reactions['FUEL']['ingredients']:
        wishlist[key] = reactions['FUEL']['ingredients'][key] * quantity 

    while len(wishlist) > 0:
        # select an arbitrary item from the wishlist
        next_ingredient = next(iter(wishlist.items()))

        # create the item from the wishlist, adding new items to the wishlist (or updating ore required if terminal) accordingly
        wishlist, leftovers, ore_required = procure_ingredient(next_ingredient, reactions, wishlist, leftovers, ore_required)
        
        # if item is in leftovers, remove it from wishlist (as we already have it)
        wishlist, leftovers = consolidate_lists(wishlist, leftovers)
   
    if ore_required < available:
        return True
    return False

def procure_ingredient(i_tuple, r_dict, wishlist, leftovers, ore):
    i = i_tuple[0]
    n = i_tuple[1]
    recipe = r_dict[i]
    
    # calculate batches required
    batch_size = recipe['quantity']
    required_batches = math.ceil(n / batch_size)
    extra_production = batch_size * required_batches - n

    # add new ingredients to the wishlist or ore to ore required
    for ingredient in recipe['ingredients'].keys():
        if ingredient == 'ORE':
            ore += recipe['ingredients'][ingredient] * required_batches
        else:
            wishlist[ingredient] += recipe['ingredients'][ingredient] * required_batches
    
    # delete the item from the wishlist (as we've repaced it with antecedents)
    leftovers[i] += extra_production
    del wishlist[i]
    return wishlist, leftovers, ore


# consolidate our leftovers into our wishlist
def consolidate_lists(wishlist, leftovers):
    for key, value in leftovers.items():
        if value != 0:
            if key in wishlist:
                x = min(value, wishlist[key])
                wishlist[key] -= x
                leftovers[key] -= x
                if wishlist[key] == 0:
                    del wishlist[key]
        
    return wishlist, leftovers 


if __name__ == "__main__":
    main()