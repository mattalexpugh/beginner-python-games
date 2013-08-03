#!/usr/bin/python
"""
The classic mobile phone game, for a UNIX-system near you!
"""

from time import sleep

import sys, random, tty, termios, signal

snake = []
head = None
position = None
score = 0
food = None

width = 20
height = 15


# Define our directions

UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4

direction = RIGHT # Default direction


def generate_blankframe():
    global width
    global height

    blankframe = []

    # Our psuedo-framebuffer is y * x of these blank lines
    for i in range(height):
        line = []

        for j in range(width):
            line.append(' ')

        blankframe.append(line)

    return blankframe

def generate_food():
    global width
    global height
    global snake

    candidate = (random.randint(0, width), random.randint(1, height))

    if candidate in snake:
        candidate = generate_food()

    return candidate

def clear_screen():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def draw_screen():
    global snake
    global head
    global width
    global height
    global score

    clear_screen()

    framebuffer = generate_blankframe()
    framebuffer[0] = "Score: " + str(score)
    output_buffer = []

    # Fill in the blanks with the game details
    for x in range(width):
        for y in range(height):
            coord = (x, y)

            if coord == head:
                framebuffer[y][x] = 'O'
            elif coord in snake:
                framebuffer[y][x] = 'x'
            elif coord == food:
                framebuffer[y][x] = '.'


    for line in framebuffer:
        output_line = ''.join(line)
        output_buffer.append(output_line)

    for line in output_buffer:
        print line

def game_over(new_head):
    print new_head
    print snake
    sleep(2)

    print "You lose!"
    sys.exit(1)

def move_snake():
    global snake
    global head
    global direction
    global food
    global score

    global UP
    global RIGHT
    global DOWN
    global LEFT

    new_head = None

    if direction == LEFT:
        new_head = (head[0] - 1, head[1])
    elif direction == DOWN:
        new_head = (head[0], head[1] + 1)
    elif direction == RIGHT:
        new_head = (head[0] + 1, head[1])
    elif direction == UP:
        new_head = (head[0], head[1] - 1)

    if new_head in snake:
        game_over(new_head)

    new_snake = [new_head]
    new_snake.extend(snake)

    if new_head == food:
        food = generate_food()
        score += 1
    else:
        new_snake = new_snake[:-1]

    head = new_head
    snake = new_snake

def get_character():
    # Adapted from http://code.activestate.com/recipes/134892/
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def wait_for_user_input():
    # Adapted from http://www.garyrobinson.net/2009/10/non-blocking-raw_input-for-python.html

    class AlarmHandler(Exception):

        def __call__(self):
            pass

    def alarm_handler(signum, frame):
        raise AlarmHandler

    signal.signal(signal.SIGALRM, alarm_handler)
    signal.alarm(1)

    try:
        inp = ord(get_character())
        signal.alarm(0)
        return inp
    except AlarmHandler:
        inp = None

    signal.signal(signal.SIGALRM, signal.SIG_IGN)

    return inp

head = (10, 10)
snake = [(10, 10), (10, 11), (10, 12)]
food = generate_food()
draw_screen()

for i in range(100):
    move_snake()
    draw_screen()

    inp = wait_for_user_input()

    """
    WASD Controls

    W (119) = UP
    S (115) = DOWN
    D (100)= RIGHT
    A (97) = LEFT
    """
    if inp:
        if inp == 119:
            direction = UP
        elif inp == 115:
            direction = DOWN
        elif inp == 100:
            direction = RIGHT
        elif inp == 97:
            direction = DOWN
