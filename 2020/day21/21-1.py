'''
DAY 21-1: Finding allergen free foods

The key observation here is that allergens match ingredients on a one to one 
basis, and we are only interested in determining the allergens that appear on 
our list.

Here we process into a food dictionary (keeping track of the input) and an 
allergen dictionary that keeps track of which ingredients could correspond 
with which allergen (present in all the dishes the allergen is listed for).

The ingredients that are not on any of these allergy list are totalled to give
the answer
'''

import pprint
from collections import defaultdict

def main():
    with open('day21/21-1-input.txt', 'r') as open_file:
        input_data = open_file.read()

    food_list = input_data.split('\n')
    
    # create dictionary of foods and set of allergens
    food_dict, allergens_set = foods_to_dict(food_list)
    print(allergens_set)
    
    # create dictionary of allergens denoting which foods they appear in
    allergen_dict = {}
    for allergen in allergens_set:
        in_foods_list = []
        for food in food_dict.keys():
            if allergen in food_dict[food]['allergens']:
                in_foods_list.append(food)
        allergen_dict[allergen] = {'foods': in_foods_list}
    
    # update dictionary of allergens denoting which ingredients they could possibly be
    # they could be any of the ingredients that appear in ALL the foods that the allergen is listed for
    # create set of ingredients that could be at least one allergen
    all_possibilities = set()
    for allergen in allergen_dict.keys():
        food_indices = allergen_dict[allergen]['foods']
        foods = []       
        for i in food_indices:
            foods.append(food_dict[i]['ingredients'])
        allergen_dict[allergen]['possible_foods'] = find_common(foods)
        all_possibilities.update(find_common(foods))
    
    pprint.pprint(allergen_dict)
    print(all_possibilities)

    total = 0
    for food in food_dict:
        for ingredient in food_dict[food]['ingredients']:
            if ingredient not in all_possibilities:
                total += 1
    
    print(total)
    

# transform input to dictionary
def foods_to_dict(food_list):
    food_dict = {}
    allergens_set = set()
    for i, food in enumerate(food_list):
        ingredients = food.split(' (contains ')[0].split(' ')
        allergens = food.split(' (contains ')[1][:-1].split(', ')
        food_dict[i] = {'ingredients': ingredients, 'allergens': allergens}
        allergens_set.update(allergens)
    return food_dict, allergens_set


# find common ingredients in a list of foods
def find_common(lists):
    result = set(lists[0])
    for s in lists[1:]:
        result.intersection_update(s)
    return result


if __name__ == "__main__":
    main()