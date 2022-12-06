'''
DAY 13-2: (Intcode) Playing breakout 

Now we need to simulate playing breakout by providing the appropriate inputs at each frame 
(move the paddle). After some manual experimentation to figure out the behavior of the game,
we can automate this to save (a lot) of time.

From observation, the ball only travels diagonally (at some rotation of a (1,1) vector). As
the paddle is only one frame long and can move as fast as the ball, this just means we can
get the paddle to always track the x position of the ball and provide the appropriate inputs.

For fun and to understand the arcade machine behavior, other functions have been added to print
the state of the game to the console
''' 
import copy
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from intcode import Intcode_computer

def main():
    with open('day13/13-1-input.txt','r') as input_file:
        input_contents = input_file.read()
    
    starting_memory = [int(x) for x in input_contents.split(',')]
    starting_memory[0] = 2

    grid = create_starting_grid()
    score = 0
    paddle_x_pos = 21
    iterations = 0

    arcade_cabinet = Intcode_computer(starting_memory, input_queue=[], suppress_notifications=True)
    while True:        
        if arcade_cabinet.status == 'halt':
            print('Game Over!')
            break
        arcade_cabinet.run()        
        grid, score, ball_x_pos = process_updates(grid, arcade_cabinet.output_queue, score)
        arcade_cabinet.clear_output_queue()
        
        # periodically print game state to the console
        if iterations % 1000 == 0:
            print('Iteration:', iterations)
            print_grid(copy.deepcopy(grid))
            print('Current score:', score, '\n\n')
        movement = choose_movement(paddle_x_pos, ball_x_pos)
        arcade_cabinet.add_to_input_queue(movement)
        paddle_x_pos += movement
        iterations += 1

    print('Final score:', score)


# pick the appropriate paddle movement based on x position of the ball
def choose_movement(paddle, ball):
    if ball > paddle:
        return 1
    if ball < paddle:
        return -1
    if ball == paddle:
        return 0


# create a blank grid of the appropriate size
def create_starting_grid():
    grid = []
    for y in range(24):
        row = []
        for x in range(42):
            row.append(0)
        grid.append(row)
    return grid


# print the current state of the game
def print_grid(grid):
    print_chars = {0: ' ', 1: '*', 2: '#', 3: '=', 4: 'o'}
    for row in grid:
        for i, pixel in enumerate(row):
            row[i] = print_chars[pixel]
        print(''.join(row))


# get the current output queue from the arcade machine and make the changes to the game state
def process_updates(grid, updates, score):   
    ball_x_pos = 0
    for i in range(len(updates) // 3):
        if updates[i * 3] == -1:
            score = updates[i*3 + 2]
        else:
            grid[updates[i*3 + 1]][updates[i*3]] = updates[i*3 + 2]
            if updates[i*3 + 2] == 4:
                ball_x_pos = updates[i*3]
    return grid, score, ball_x_pos


if __name__ == "__main__":
    
    main()