# A Snake Game for the Adafruit CLUE

I wanted to show off what you can do using the CLUE simulator on the [Device Simulator Express](https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress) VS Code extension! Even without the CLUE on hand, I was able to make this fun little game 👩‍💻.

I have a tutorial here in case anyone wants to follow it on Device Simulator Express too!

## Tutorial:
### STEP 1: 
Get some imports going!

```python
import board
from adafruit_clue import clue
from adafruit_display_shapes.circle import Circle
import displayio
import time
import random
```

### STEP 2: 
Create Group for the display to focus on.

```python
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

```

### STEP 3: 
Create a red dot in the middle of the screen to start our snake! Also, put an infinite loop at the end so that the dot stays on the screen.

```python
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
    pass
```

### STEP 4: 
Make the red dot creep across the screen.

```python
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
```

### STEP 5: 
Re-factor the code to support every direction

```python
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


# lookup for x and y offsets given the direction
new_position = {
    "left":(-1,0),
    "up":(0,-1),
    "right":(1,0),
    "down":(0,1)
}

# you can change this value to "up", "right", or "down" to change the direction of the movement.
first_direction = "left"
# game loop
while True:
    offset_tuple = new_position[first_direction]
    first_dot.x += offset_tuple[0]
    first_dot.y += offset_tuple[1]
    pass
```

### STEP 6: 
Add initial work to get buttons to control where the snake goes.

```python
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
```

### STEP 7: 
Add extra conditionals so that the code doesn't count holding down a button as multiple commands to change direction. This should stabilize the direction control.

```python
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


# If the last_pressed_button is not the button that
# is currently being pushed, we know that the button
# has not been registered yet
last_pressed_button = None

# game loop
direction = "left"
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
    first_dot.x += offset_tuple[0]
    first_dot.y += offset_tuple[1]

    direction = new_direction
```

### STEP 8: 
Add a dot for snake food and detect when you hit it. When you hit it, reset the location. Also, speed up the dot.

```python
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

# let's start the points at 0 
points = 0

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

    # check whether the snake ate the food!

    # give the overlap check an uncertainty of 5
    # so that our snake can still eat the food,
    # even if it's a little off
    if (has_overlap(food_dot, first_dot, 5)):
        points +=1
        print("You got a point! Now you're at " + str(points) + " point(s)")
        reset_food()
```
### STEP 9:
End the game if you hit the edge of the screen.

```python
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

# let's start the points at 0 
points = 0

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
```

### STEP 10:
Add some fancy lights for adding points and losing the game.

```python
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
```

### STEP 11:
Reformat the code to support multiple dots.

```python
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

# make a list of the snake's dots
snake_dots = []

# make a dot for food and show it on the screen
food_dot = make_dot(x=random.randint(5,235),y=random.randint(5,235),fill=clue.AQUA)
stuff_on_screen.append(food_dot)

# we gotta get a first dot going!
add_dot(120,120)

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

    # the first element of the snake_dots array is the current leading dot
    # use this to determine the position of the newest head dot
    old_lead_dot = snake_dots[0]
    old_lead_dot.x += offset_tuple[0] *5
    old_lead_dot.y += offset_tuple[1] *5

    direction = new_direction

    # make sure that it isn't hitting any of the screen's sides
    if old_lead_dot.x > 240 or old_lead_dot.x < 0 or old_lead_dot.y > 240 or old_lead_dot.y < 0:
        game_over()

    # check whether the snake ate the food!
    
    # give the overlap check an uncertainty of 5
    # so that our snake can still eat the food,
    # even if it's a little off
    if (has_overlap(food_dot, old_lead_dot, 5)):
        points +=1
        print("You got a point! Now you're at " + str(points) + " point(s)")
        reset_food()
        
        # change the neopixel color
        set_neopixel()
```

### STEP 12
Instead of constantly moving the current dot, create a new dot each time and remove the oldest dot. This will help when the snake has a long tail, as this will only require the screen to refresh twice when the snake is moving.

```python
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

        # change the neopixel color
        set_neopixel()
```

### STEP 13:
Add length to snake when the snake eats food and also detect when you collide with the tail.

```python
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
```

### And you're done! 🤖