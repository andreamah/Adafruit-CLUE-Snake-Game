# A Snake Game for the Adafruit CLUE

I wanted to show off what you can do using the CLUE simulator on the [Device Simulator Express](https://marketplace.visualstudio.com/items?itemName=ms-python.devicesimulatorexpress) VS Code extension! Even without the CLUE on hand, I was able to make this fun little game 👩‍💻.

I have a tutorial here in case anyone wants to follow it on Device Simulator Express too!

## Tutorial

Clicking on any header will show the differences from the prior step, using GitHub's differencing view.

Clicking each link will show the differences in that commit.

### [STEP 1: Get some imports going](/../../commit/346d185)

### [STEP 2: Create Group for the display to focus on](/../../commit/ad698fc)

### [STEP 3: Display a (starting) snake](/../../commit/6693fb1)

Create a red dot in the middle of the screen to start our snake! Also, put an infinite loop at the end so that the dot stays on the screen.

### [STEP 4: Make the red dot creep across the screen](/../../commit/a2c3097)

### [STEP 5: Re-factor the code to support every direction](/../../commit/808415c)

### [STEP 6: Add initial work to get buttons to control where the snake goes](/../../commit/c9d499d)

### [STEP 7:  Stabilize directional controls](/../../commit/b7bfaeb)

Add extra conditionals so that the code doesn't count holding down a button as multiple commands to change direction. This should stabilize the direction control.

### [STEP 8: Add snake food and speed up dot](/../../commit/aac8e0a)

Add a dot for snake food and detect when you hit it. When you hit it, reset the location. Also, speed up the dot.

### [STEP 9: End the game if you hit the edge of the screen](/../../commit/43c8bb7)

### [STEP 10: Add some fancy lights for adding points and losing the game](/../../commit/b8e3167)

### [STEP 11: Reformat the code to support multiple dots](/../../commit/30dbbc1)

### [STEP 12: Improve performance for long snakes](/../../commit/bc21338)

Instead of constantly moving the current dot, create a new dot each time and remove the oldest dot. This will help when the snake has a long tail, as this will only require the screen to refresh twice when the snake is moving.

### [STEP 13: Grow snake and detect collision with tail](/../../commit/8e512ef)

Add length to snake when the snake eats food and also detect when you collide with the tail.

### And you're done! 🤖
