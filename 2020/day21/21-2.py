'''
DAY 21-2: Matching ingredients to allergens

This builds directly off the intermediate solution to 21-1. As this already
includes lists of which ingredients could be which allergens, we just
need to do a 'sudoku slice' on it. If one allergen can only be one ingredient,
then that ingredient should be locked in and removed from the other possibility
lists.

This leaves a unique ingredient for each allergen.
'''

import pprint
from collections import defaultdict
import copy

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
    for allergen in allergen_dict.keys():
        food_indices = allergen_dict[allergen]['foods']
        foods = []       
        for i in food_indices:
            foods.append(food_dict[i]['ingredients'])
        allergen_dict[allergen]['possible_foods'] = list(find_common(foods))
    
    pprint.pprint(allergen_dict)

    # iterate over dictionary and remove the uniquely identifiable ingredients from the rest of the lists
    # when there are no more updates to make, return the dictionary
    stable = False
    while not stable:
        stable = True
        check_dict = copy.deepcopy(allergen_dict)
        for a in allergen_dict:
            if len(allergen_dict[a]['possible_foods']) == 1:
                unique_food = allergen_dict[a]['possible_foods'][0]
                for b in allergen_dict:
                    if a != b and unique_food in allergen_dict[b]['possible_foods']:                        
                        allergen_dict[b]['possible_foods'].remove(unique_food)
        if check_dict != allergen_dict:
            stable = False
    
    # sort the list alphabetically by allergen to get the result string
    allergen_list = []
    for a in allergen_dict:
        allergen_list.append(a)
    allergen_list = sorted(allergen_list)

    result_string = ''
    for a in allergen_list:
        result_string = result_string + ',' + allergen_dict[a]['possible_foods'][0]
    
    print(result_string[1:])


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