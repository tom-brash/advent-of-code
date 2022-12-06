'''
Day 14-2: The elf recipe game II

Somewhat surprisingly, this can be run with functinoally the same code, except keeping track of 
the last 6 recipes found. This makes it relatively slow (~15s) as the recipes required is in the order
of ~20m. There are absolutely efficiencies to take advantage of here, but are not strictly neccesary
'''

def main():
    with open('day14/14-1-input.txt', 'r') as open_file:
        n = int(open_file.read())
    
    total_recipes = 2
    recipes = {0: 3, 1: 7}

    elf_1 = 0
    elf_2 = 1

    new_recipes = {}  # memoize the process to avoid string conversions
    search_string = str(n)
    last_6 = '000037'
    found = False

    while not found:
        s = recipes[elf_1] + recipes[elf_2]
        if s in new_recipes:
            new = new_recipes[s]
        else:
            new = [int(d) for d in str(s)]
            new_recipes[s] = new
        
        for recipe in new:
            recipes[total_recipes] = recipe
            total_recipes += 1
            last_6 = last_6[1:] + str(recipe)
            if last_6 == search_string:
                found = True
                print('Found! After', total_recipes - 6, 'recipes!')

        elf_1 = (recipes[elf_1] + elf_1 + 1) % total_recipes
        elf_2 = (recipes[elf_2] + elf_2 + 1) % total_recipes

            
if __name__ == '__main__':
    main()