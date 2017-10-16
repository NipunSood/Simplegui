# Run code at http://www.codeskulptor.org/
import simplegui
# template for "Stopwatch: The Game"

# define global variables
t=0
d=0
win=0
total=0
running=True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    a,b,c,d=0,0,0,0
    d=t%10
    c=t/10
    c=c%10
    b=t/100
    if b>=6:
        a=b/6
    b=b%6
    return str(a)+":"+str(b)+str(c)+"."+str(d)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global running
    timer.start()
    running=True
def stop():
    global d,win,total,running
    timer.stop()
    if running:
        if not d:
            win+=1
        total+=1
    running=False
    
def reset():
    global t,running,win,total
    win,total=0,0
    running=False
    stop()
    t=0
    

# define event handler for timer with 0.1 sec interval
def tick():
    global t
    t+=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t),(60,100),32,"white")
    canvas.draw_text(str(win)+"/"+str(total),[130,30],32,"green")
    
# create frame
frame=simplegui.create_frame("Home",200,200)

timer=simplegui.create_timer(100,tick)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)


# start frame
frame.start()

# Please remember to review the grading rubric
