"""This is a python project that makes use of the dokusan library to create sudoku puzzles"""
from dokusan import generators
import numpy as np
my_array=generators.random_sudoku(avg_rank=100)

#convert the array to a 9*9 grid using numpy
grid=np.array(list(str(my_array)))

print(grid.reshape(9,9))
