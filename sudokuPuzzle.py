"""This is a python project that makes use of the dokusan library to create sudoku puzzles"""
from dokusan import generators
import numpy as np

import sys,pygame as pg
pg.init()
screen_size=750,750
screen=pg.display.set_mode(screen_size)

def generate_puzzle(difficulty):
    my_array=generators.random_sudoku(avg_rank=difficulty)

    grid=np.array(list(str(my_array)), dtype=int)

    return(grid.reshape(9,9))


puzzle=generate_puzzle(100)

def background():
    #code for it
    screen.fill(pg.Color("White"))
    pg.draw.rect(screen,pg.Color("pink"),pg.Rect(15,15,720,720),10)
    i=1
    #draw the grids
    while (i*80)<720:
        line_width=5 if i%3>0 else 10
        pg.draw.line(screen,pg.Color("pink"),pg.Vector2(((i*80)+15),15),pg.Vector2(((i*80)+15),735),line_width)
        pg.draw.line(screen,pg.Color("pink"),pg.Vector2((15,(i*80)+15)),pg.Vector2(735,((i*80)+15)),line_width)

        i+=1

def draw_numbers():
    font = pg.font.Font(None, 60)
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] != 0:  # Only draw non-zero numbers
                num_text = font.render(str(puzzle[row][col]), True, pg.Color("black"))
                screen.blit(num_text, (col * 80 + 35, row * 80 + 25))  

#set up a game loop
def gameLoop():
    for event in pg.event.get():
        if event.type==pg.QUIT:sys.exit()
    background() 
    draw_numbers()
    pg.display.flip()   

while 1:
    gameLoop()        
