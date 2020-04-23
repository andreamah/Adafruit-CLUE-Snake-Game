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

# add a dot to the snake
def add_dot(x,y,position=-1):
    global snake_dots
    global stuff_on_screen
    new_dot = make_dot(x,y,clue.RED,5)
    snake_dots.insert(position,new_dot)
    stuff_on_screen.append(new_dot)

# remove a dot from the end of the snake
def pop_end_dot():
    global snake_dots
    global stuff_on_screen
    end_dot = snake_dots.pop()
    stuff_on_screen.remove(end_dot)

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

new_position = {
    "left":(-1,0),
    "up":(0,-1),
    "right":(1,0),
    "down":(0,1)
}


# beginning of the main program

# make a group and make sure that the CLUE's
# display is focused on this group
stuff_on_screen = displayio.Group(max_size=100)
board.DISPLAY.show(stuff_on_screen)

# make a list of the snake's dots
snake_dots = []

# make a dot for food and show it on the screen
food_dot = make_dot(x=random.randint(5,235),y=random.randint(5,235),fill=clue.AQUA)
stuff_on_screen.append(food_dot)

# we gotta get a first dot going!
add_dot(120,120)

# the dot heads left first
direction = "left"

# to make sure that holding the A/B buttons
# would not keep turning our snake

# If the last_pressed_button is not the button that
# is currently being pushed, we know that the button
# has not been registered yet
last_pressed_button = None

# let's start the points at 0 and set the neopixel to the first color
points = 0
set_neopixel()

# start the game loop
while True:
    # NOTE: uncomment if not on simulator
    time.sleep(0.1)

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

    # let's get the new co-ordinates given the new direction
    new_x_offset,new_y_offset = new_position[new_direction]
    direction = new_direction

    # the first element of the snake_dots array is the current leading dot
    # use this to determine the position of the newest head dot
    old_lead_dot = snake_dots[0]

    # if we just move by 1 pixel each loop, that might be too slow...
    # so we're moving by 5 pixels
    x = old_lead_dot.x + (new_x_offset * 5)
    y = old_lead_dot.y + (new_y_offset * 5)

    # let's add the new head dot and remove the last one
    # so that our snake keeps moving
    add_dot(x,y,0)
    pop_end_dot()
    
    # and let's grab the new head dot so that we can determine where we are!
    new_lead_dot = snake_dots[0]

    # make sure that the snake isn't running into itself by
    # looking at all dots aside from the first dot and making sure that
    # the first dot doesn't overlap with any of the others
    for dot in snake_dots[1:]:
        if (has_overlap(dot,new_lead_dot)):
            game_over()

    # make sure that it isn't hitting any of the screen's sides
    if new_lead_dot.x > 240 or new_lead_dot.x < 0 or new_lead_dot.y > 240 or new_lead_dot.y < 0:
        game_over()

    # check whether the snake ate the food!

    # give the overlap check an uncertainty of 5
    # so that our snake can still eat the food,
    # even if it's a little off
    if (has_overlap(food_dot, new_lead_dot, 5)):
        points +=1
        print("You got a point! Now you're at " + str(points) + " point(s)")
        reset_food()

        # make the snake longer!
        add_dot(x,y)
        
        # change the neopixel color
        set_neopixel()

        