"""sudoku grid using pygame"""
import sys,pygame as pg

pg.init()
screen_size=750,750
screen=pg.display.set_mode(screen_size)

from dokusan import generators
import numpy as np
my_array=generators.random_sudoku(avg_rank=100)

#convert the array to a 9*9 grid using numpy
grid=np.array(my_array)

print(grid)