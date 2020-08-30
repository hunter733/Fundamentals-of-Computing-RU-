# template for "Stopwatch: The Game"
import simplegui

# define global variables
s = 0
message = "0:00.0"
x = 0
y = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A= t//600
    B= (((t//10)%60)//10)
    C= (((t//10)%60)%10)
    D= t%10

    return str(A)+":"+str(B)+str(C)+"."+str(D)


# define event handlers for buttons; "Start", "Stop", "Reset"
def start1():
    t.start()


def stop2():
    t.stop()
    global s,x,y
    x+=1
    if s%10 == 0:
        y+=1



def reset3():
    t.stop()
    global s,x,y,message
    s=0
    message= "0:00.0"
    x=0
    y=0


# define event handler for timer with 0.1 sec interval
def create_timer():
    global s,message
    s+=1
    message=format(s)


# define draw handler
def draw(canvas):
    canvas.draw_text(message,[100,100],36,"green")
    canvas.draw_text(str(x)+"/"+str(y),[240,30],32,"red")
# create frame
f= simplegui.create_frame("stopwtach",300,200)


# register event handlers
t=simplegui.create_timer(100,create_timer)
f.set_draw_handler(draw)
f.add_button("start",start1,100)
f.add_button("stop",stop2,100)
f.add_button("reset",reset3,100)

# start frame
f.start()


# Please remember to review the grading rubric
