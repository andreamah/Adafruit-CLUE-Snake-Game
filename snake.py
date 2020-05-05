import board
from adafruit_clue import clue
from adafruit_display_shapes.circle import Circle
import displayio
import time
import random

# create a new dot
def make_dot(x,y,fill,size=5):
    # use the group to set x and y position
    # so that the display re-draws the dot when
    # x and y is set.
    dot_group = displayio.Group(x=x,y=y)
    dot = Circle(0,0, size, fill=fill)
    dot_group.append(dot)
    return dot_group 

# make a group and make sure that the CLUE's
# display is focused on this group
stuff_on_screen = displayio.Group(max_size=100)
board.DISPLAY.show(stuff_on_screen)

first_dot = make_dot(120,120,clue.RED,5)
stuff_on_screen.append(first_dot)

# game loop
while True:
    first_dot.x -=1
    pass
