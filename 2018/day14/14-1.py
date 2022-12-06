'''
Day 14-1: The elf recipe game

Here the problem is small enough that we can just implement the logic of the game and run
it for the required number of steps naively (and still have it run in <1s)
'''

def main():
    with open('day14/14-1-input.txt', 'r') as open_file:
        n = int(open_file.read())
    
    total_recipes = 2
    recipes = {0: 3, 1: 7}

    elf_1 = 0
    elf_2 = 1

    new_recipes = {}  # memoize the process to avoid string conversions
    answer = ''

    while total_recipes < n + 10:
        s = recipes[elf_1] + recipes[elf_2]
        if s in new_recipes:
            new = new_recipes[s]
        else:
            new = [int(d) for d in str(s)]
            new_recipes[s] = new
        
        for recipe in new:
            recipes[total_recipes] = recipe
            total_recipes += 1
            if total_recipes > n:
                answer += str(recipe)

        elf_1 = (recipes[elf_1] + elf_1 + 1) % total_recipes
        elf_2 = (recipes[elf_2] + elf_2 + 1) % total_recipes

    
    print(answer[:10])  # if the last step made two recipes, there may be 11 recipes made above the n given as input
        

if __name__ == '__main__':
    main()