import board
from adafruit_clue import clue
from adafruit_display_shapes.circle import Circle
import displayio
import time
import random

# make a group and make sure that the CLUE's
# display is focused on this group
stuff_on_screen = displayio.Group(max_size=100)
board.DISPLAY.show(stuff_on_screen)
