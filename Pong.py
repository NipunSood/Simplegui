# Implementation of classic arcade game Pong
# Run code at http://www.codeskulptor.org/

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
ball_pos=[WIDTH/2,HEIGHT/2]
vel = [-40.0 / 60.0,  5.0 / 60.0]
paddle1_pos=HEIGHT/2
paddle2_pos=HEIGHT/2
paddle1_vel=0
paddle2_vel=-0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, vel # these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]
    x=random.randrange(120, 240)
    y=random.randrange(60, 180)
    if direction=="RIGHT":
        vel = [x/ 60.0,-y / 60.0]
    elif direction=="LEFT":
        vel = [-x / 60.0,-y / 60.0]
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1] 
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1=0
    score2=0
    spawn_ball("LEFT")

def draw(canvas):
    global score1, score2,paddle2_vel,paddle1_vel, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        vel[1] = -vel[1]
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            vel[0] = -(vel[0] * 1.1)
        else:
            score2+=1
            spawn_ball("RIGHT")
    if ball_pos[0] + BALL_RADIUS >= WIDTH - PAD_WIDTH:
        if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT:
            vel[0] = -(vel[0] * 1.1)
        else:
            score1+=1
            spawn_ball("LEFT")
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += vel[0]
    ball_pos[1] += vel[1]        
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"white","white")
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos+ paddle1_vel-HALF_PAD_HEIGHT<=0 or paddle1_pos+paddle1_vel+HALF_PAD_HEIGHT>=HEIGHT:
        paddle1_vel=0
    if paddle2_pos+paddle2_vel-HALF_PAD_HEIGHT<=0 or paddle2_pos+paddle2_vel+HALF_PAD_HEIGHT>=HEIGHT:
        paddle2_vel=0
    paddle1_pos+=paddle1_vel 
    paddle2_pos+=paddle2_vel        
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT],[HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT],[WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    # draw scores
    canvas.draw_text(str(score1),(130,40),50,"blue")
    canvas.draw_text(str(score2),(430,40),50,"blue")
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=7
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=7
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=7
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel+=7
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel=0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel=0
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel=0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel=0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset",new_game,50)
# start frame
new_game()
frame.start()
