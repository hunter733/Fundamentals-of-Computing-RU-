# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
pad_vel = [0, 5]
score1 = 0
score2 = 0
ball_pos = [WIDTH / 2, HEIGHT / 2]
padL_pos = [HALF_PAD_WIDTH, HEIGHT/2]
padR_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
padL_vel = 0
padR_vel = 0
direction = 0
ball_vel = [direction, 0]



# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball():
    global ball_pos, ball_vel # these are vectors stored as lists
    global direction
    ball_vel = [direction, -3]
    ball_pos = [WIDTH / 2, HEIGHT / 2]

# define event handlers
def new_game():
    global padR_pos, padL_pos, padL_vel, padR_vel  # these are numbers
    global score1, score2, direction  # these are ints
    padL_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    padR_pos = [WIDTH - HALF_PAD_WIDTH, HEIGHT/2]
    score1 = 0
    score2 = 0
    direction = random.choice([-3, -2, 2, 3])
    spawn_ball()


def new_ball():
    global direction
    direction = random.choice([-3, -2, 2, 3])
    spawn_ball()

#def score(direction)

def draw(canvas):
    global padL_pos, padR_pos, ball_pos, ball_vel
    global  score1, score2, direction

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball

    #gutter ball X-AXIS
    if ball_vel[0] < 0:
        if ball_pos[0]  < (PAD_WIDTH+ BALL_RADIUS):
            if (ball_pos[1]) > (padL_pos[1] + HALF_PAD_HEIGHT):
                score2 += 1
                direction = random.choice([-2, -3])
                spawn_ball()
            if (ball_pos[1]) < (padL_pos[1] - HALF_PAD_HEIGHT):
                score2 += 1
                direction = random.choice([2, 3])
                spawn_ball()
            else:
                ball_vel[0] = - ball_vel[0]
    if ball_vel[0] > 0:
        if (ball_pos[0] + BALL_RADIUS) > (WIDTH - PAD_WIDTH):
            if (ball_pos[1]) > (padR_pos[1] + HALF_PAD_HEIGHT):
                score1 += 1
                direction = random.choice([2, 3])
                spawn_ball()
            if (ball_pos[1]) < (padR_pos[1] - HALF_PAD_HEIGHT):
                score1 += 1
                direction = random.choice([-2, -3])
                spawn_ball()
            else:
                ball_vel[0] = - ball_vel[0]

    #wall ball Y-AXIS
    if ball_pos[1] > (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] < (0 + BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]

    ball_pos[1] += ball_vel[1]
    ball_pos[0] += ball_vel[0]


    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")

    # update paddle's vertical position, keep paddle on the screen
    if padL_vel < 0:
        if padL_pos[1] > HALF_PAD_HEIGHT:
            padL_pos[1] = padL_pos[1] + padL_vel
    if padL_vel > 0:
        if padL_pos[1] < HEIGHT-HALF_PAD_HEIGHT:
            padL_pos[1] = padL_pos[1] + padL_vel
    if padR_vel < 0:
        if padR_pos[1] > HALF_PAD_HEIGHT:
            padR_pos[1] = padR_pos[1] + padR_vel
    if padR_vel > 0:
        if padR_pos[1] < HEIGHT-HALF_PAD_HEIGHT:
            padR_pos[1] = padR_pos[1] + padR_vel

    # draw paddles

    canvas.draw_polygon([(0, padL_pos[1]-HALF_PAD_HEIGHT), (PAD_WIDTH, padL_pos[1]-HALF_PAD_HEIGHT), (PAD_WIDTH, padL_pos[1]+HALF_PAD_HEIGHT), (0, padL_pos[1]+HALF_PAD_HEIGHT)], 1, "White", "White")
    canvas.draw_polygon([(padR_pos[0]-HALF_PAD_WIDTH, padR_pos[1]-HALF_PAD_HEIGHT), (WIDTH,  padR_pos[1]-HALF_PAD_HEIGHT), (WIDTH,  padR_pos[1]+HALF_PAD_HEIGHT), (padR_pos[0]-HALF_PAD_WIDTH, padR_pos[1]+HALF_PAD_HEIGHT)], 1, "White", "White")

    # draw scores
    canvas.draw_text(str(score1), [(WIDTH / 2 - 48), 30], 24, "White")
    canvas.draw_text(str(score2), [(WIDTH / 2 + 36), 30], 24, "White")


def keydown(key):
    global padR_vel, padL_vel
    if key == simplegui.KEY_MAP["down"]:
        if padR_pos[1] < (HEIGHT - HALF_PAD_HEIGHT):
            padR_vel = 5
    if key == simplegui.KEY_MAP["up"]:
        if padR_pos[1] > HALF_PAD_HEIGHT:
            padR_vel = -5

    if key == simplegui.KEY_MAP["s"]:
        if padL_pos[1] < (HEIGHT - HALF_PAD_HEIGHT):
            padL_vel = 5
    if key == simplegui.KEY_MAP["w"]:
        if padL_pos[1] > HALF_PAD_HEIGHT:
            padL_vel = -5

def keyup(key):
    global padR_vel, padL_vel
    if key == simplegui.KEY_MAP["down"]:
        padR_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        padR_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        padL_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        padL_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game)
frame.add_button("New ball", new_ball)

# start frame
frame.start()
new_game()
