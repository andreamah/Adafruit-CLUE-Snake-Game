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

# some dictionaries to help us choose new directions
# for our snake
direction_right_of={
    "left":"up",
    "up":"right",
    "right":"down",
    "down":"left"
}

direction_left_of={
    "left":"down",
    "up":"left",
    "right":"up",
    "down":"right"
}

# lookup for x and y offsets given the direction
new_position = {
    "left":(-1,0),
    "up":(0,-1),
    "right":(1,0),
    "down":(0,1)
}

# game loop
direction = "left"
while True:
    if (clue.button_a):
        new_direction = direction_left_of[direction]
    elif (clue.button_b):
        new_direction = direction_right_of[direction]
    else:
        new_direction = direction

    offset_tuple = new_position[new_direction]
    first_dot.x += offset_tuple[0]
    first_dot.y += offset_tuple[1]

    direction = new_direction
