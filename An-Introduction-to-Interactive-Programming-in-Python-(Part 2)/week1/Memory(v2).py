import simplegui
import random

num = 8
CardNumber = range(num)*2
exposed = [False]*len(CardNumber)
pre = None
post = None
counter = 0


def new_game():
    global CardNumber, state, counter, exposed
    random.shuffle(CardNumber)
    exposed = [False]*len(CardNumber)
    state = 0
    counter = 0
    label.set_text("Turns = " + str(counter))


def mouseclick(pos):
    global exposed, state, pre, post, CardNumber, counter

    idx = pos[0] / 50

    if state == 0:
        state = 1
        exposed[idx] = True
        pre = idx
        counter = 1
    elif state == 1:
        if exposed[idx] == False:
            exposed[idx] = True
            state = 2
            post = idx
    else:
        if exposed[idx] == False:
            exposed[idx] = True
            if CardNumber[pre]==CardNumber[post]:
                exposed[pre] = True
                exposed[post] = True
            else:
                exposed[pre] = False
                exposed[post] = False
            counter += 1
            state = 1
            pre = idx
    label.set_text("Turns = " + str(counter))

def draw(canvas):
    global CardNumber
    for i in range(16):
        if exposed[i]:
            canvas.draw_text(str(CardNumber[i]), [9+50*i, 75], 72, "Purple")
        else:
            canvas.draw_polygon([(i*50, 0), (50+i*50, 0), (50+i*50, 100), (i*50, 100)], 2, "Purple", "Pink")


frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label('Turns = 0')


frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


new_game()
frame.start()
