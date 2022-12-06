'''
DAY 13-2: (Intcode) (Extension) Visualizing an arcade machine

This version of 13-2 uses the same underlying functions but uses tkinter to produce
visualized output. The mechanism for this is simple, just using an ASCII representation
of the game state and changing the tk label to that representation at every step.
''' 
import copy
import tkinter as tk
import sys
import os
from time import sleep
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

    # set up visualization variables
    window = tk.Tk()
    game_state = tk.StringVar()
    game_state.set('')
    game_score = tk.StringVar()
    game_score.set('')
    lbl_game = tk.Label(window, textvariable=game_state, font='TkFixedFont', fg="yellow", bg="black")
    lbl_game.pack()
    lbl_score = tk.Label(window, textvariable=game_score, fg="red", bg="black")
    lbl_score.pack(fill=tk.X)

    while True:        
        if arcade_cabinet.status == 'halt':
            break
        arcade_cabinet.run()        
        grid, score, ball_x_pos = process_updates(grid, arcade_cabinet.output_queue, score)
        arcade_cabinet.clear_output_queue()
        
        printable = printable_grid(copy.deepcopy(grid))
        game_state.set(printable)
        game_score.set('Score: ' + str(score))
        sleep(0.05)
        window.update()

        movement = choose_movement(paddle_x_pos, ball_x_pos)
        arcade_cabinet.add_to_input_queue(movement)
        paddle_x_pos += movement
        iterations += 1

    game_score.set('Game over! Final score: ' + str(score))
    window.mainloop()

def run_game(lbl_game):
    lbl_game.text



def choose_movement(paddle, ball):
    if ball > paddle:
        return 1
    if ball < paddle:
        return -1
    if ball == paddle:
        return 0


def create_starting_grid():
    grid = []
    for y in range(24):
        row = []
        for x in range(42):
            row.append(0)
        grid.append(row)
    return grid


def printable_grid(grid):
    print_chars = {0: ' ', 1: '*', 2: '#', 3: '=', 4: 'o'}
    printable_grid = ''
    for row in grid:
        for i, pixel in enumerate(row):
            row[i] = print_chars[pixel]
        printable_grid += (''.join(row))
        printable_grid += '\n'
    return printable_grid


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