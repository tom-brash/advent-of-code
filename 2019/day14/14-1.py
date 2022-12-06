'''
DAY 14-1: Creating materials from ORE

Here we have a number of receipes and need to determine how much of the original ingredient (ORE)
is required to make FUEL. The catch here is that every ingredient needs to be made in batches, which
means that it is insufficient to simply keep track of how much ORE each ingredient requires (making
some combinations may be more efficient than others).

This means we need to keep track of the excess materials that we are producing, and remove them from
our wishlist of materials as we go
''' 
import re
from collections import defaultdict
import pprint
import math

def main():
    with open('day14/14-1-input.txt', 'r') as open_file:
        input_data = open_file.read()
    
    reaction_data = input_data.split('\n')

    # parse the inputs into a dictionary
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

    # create default dicts for available leftovers and our wishlist of materials
    leftovers = defaultdict(int)
    wishlist = defaultdict(int)
    ore_required = 0

    # create our wishlist for a single unit of fuel
    for key in reactions['FUEL']['ingredients']:
        wishlist[key] = reactions['FUEL']['ingredients'][key]


    while len(wishlist) > 0:
        # select an arbitrary item from the wishlist
        next_ingredient = next(iter(wishlist.items()))

        # create the item from the wishlist, adding new items to the wishlist (or updating ore required if terminal) accordingly
        wishlist, leftovers, ore_required = procure_ingredient(next_ingredient, reactions, wishlist, leftovers, ore_required)
        
        # if item is in leftovers, remove it from wishlist (as we already have it)
        wishlist, leftovers = consolidate_lists(wishlist, leftovers)
   
    print('Final ORE required:', ore_required)


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