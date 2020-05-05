import board
from adafruit_clue import clue
from adafruit_display_shapes.circle import Circle
import displayio
import time
import random


# put the food somewhere else on the screen
def reset_food():
    global food_dot
    food_dot.x,food_dot.y = (random.randint(5,235),random.randint(5,235))

# given an uncertainty value, see if two values are the same
def approx_equals(num_one,num_two,uncertainty):
    if (num_one + uncertainty >= num_two and num_one-uncertainty<=num_two):
        return True
    else:
        return False

# given an uncertainty value, see if two dots are overlapping
def has_overlap(dot_one,dot_two,uncertainty=0):
    if (approx_equals(dot_one.y,dot_two.y,uncertainty) and 
        approx_equals(dot_one.x, dot_two.x,uncertainty)):
        return True
    else:
        return False

# create a new dot
def make_dot(x,y,fill,size=5):
    # use the group to set x and y position
    # so that the display re-draws the dot when
    # x and y is set.
    dot_group = displayio.Group(x=x,y=y)
    dot = Circle(0,0, size, fill=fill)
    dot_group.append(dot)
    return dot_group 

# show our "game over" screen
def game_over():
    clue_data = clue.simple_text_display(text_scale=3)
    clue_data[1].text = "GAME OVER!"
    clue_data[3].text = "POINTS: " + str(points)
    clue_data.show()
    flash_lights()

# make your red light flash!
def flash_lights():
    clue.red_led = True
    time.sleep(0.1)
    clue.red_led = False
    time.sleep(0.1)

def set_neopixel():
    global points
    
    # change the neopixel color:
    new_light_color = clue.RAINBOW[points%len(clue.RAINBOW)]
    clue.pixel.fill(new_light_color)

# make a group and make sure that the CLUE's
# display is focused on this group
stuff_on_screen = displayio.Group(max_size=100)
board.DISPLAY.show(stuff_on_screen)

# make a dot for food and show it on the screen
food_dot = make_dot(x=random.randint(5,235),y=random.randint(5,235),fill=clue.AQUA)
stuff_on_screen.append(food_dot)

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


# If the last_pressed_button is not the button that
# is currently being pushed, we know that the button
# has not been registered yet
last_pressed_button = None

# game loop
direction = "left"

# let's start the points at 0 and set the neopixel to the first color
points = 0
set_neopixel()

while True:
    if (clue.button_a):
        if not last_pressed_button == "A":
            # query the direction_left_of dictionary to find
            # where to go next
            new_direction = direction_left_of[direction]
            last_pressed_button = "A"
    elif (clue.button_b):
        if not last_pressed_button == "B":
            # like above, find where to go next using the 
            # direction_right_of dictionary
            new_direction = direction_right_of[direction]
            last_pressed_button = "B"
    else:
        # otherwise, no direction change!
        new_direction = direction
        last_pressed_button = None

    offset_tuple = new_position[new_direction]
    first_dot.x += offset_tuple[0] *5
    first_dot.y += offset_tuple[1] *5

    direction = new_direction

    # make sure that it isn't hitting any of the screen's sides
    if first_dot.x > 240 or first_dot.x < 0 or first_dot.y > 240 or first_dot.y < 0:
        game_over()

    # check whether the snake ate the food!
    # give the overlap check an uncertainty of 5
    # so that our snake can still eat the food,
    # even if it's a little off
    if (has_overlap(food_dot, first_dot, 5)):
        points +=1
        print("You got a point! Now you're at " + str(points) + " point(s)")
        reset_food()
        
        # change the neopixel color
        set_neopixel()
