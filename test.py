"""sudoku grid using pygame"""
import sys,pygame as pg

pg.init()
screen_size=600,600
screen=pg.display.set_mode(screen_size)

#def background():
    #code for it
    

#set up a game loop
def gameLoop():
    for event in pg.event.get():
        if event.type==pg.QUIT:sys.exit()
    #background()    

while 1:
    gameLoop()        