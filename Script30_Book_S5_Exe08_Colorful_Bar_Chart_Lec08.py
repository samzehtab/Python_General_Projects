#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S5 Book Exc08: Colorful Bar Chart Without Gap

import turtle

def make_window(bg: str):
    '''
    Drawing a Screen
    '''
    wn = turtle.Screen()
    wn.bgcolor(bg)
    wn.title('Bar Chart')
    return wn
    
### Driver Code ###

xs = [48, 117, 200, 240, 160, 260, 220]
win = make_window(bg = 'lightgreen')

tur = turtle.Turtle()
tur.color('blue', 'blue')
tur.pensize(3)
tur.speed(0)

tur.hideturtle()
tur.up()
tur.goto(-200, -100)
tur.down()
for h in xs:
    if h >= 200:
        tur.color('blue', 'red')
        tur.begin_fill()
        tur.lt(90)
        tur.fd(h)
        tur.write('  ' + str(h))
        tur.rt(90)
        tur.fd(40)
        tur.rt(90)
        tur.fd(h)
        tur.lt(90)
        tur.end_fill()
        tur.up()
        tur.fd(10)
        tur.down()
    elif 100 <= h < 200:
        tur.color('blue', 'yellow')
        tur.begin_fill()
        tur.lt(90)
        tur.fd(h)
        tur.write('  ' + str(h))
        tur.rt(90)
        tur.fd(40)
        tur.rt(90)
        tur.fd(h)
        tur.lt(90)
        tur.end_fill()
        tur.up()
        tur.fd(10)
        tur.down()
    else:
        tur.color('blue', 'green')
        tur.begin_fill()
        tur.lt(90)
        tur.fd(h)
        tur.write('  ' + str(h))
        tur.rt(90)
        tur.fd(40)
        tur.rt(90)
        tur.fd(h)
        tur.lt(90)
        tur.end_fill()
        tur.up()
        tur.fd(10)
        tur.down()

win.mainloop()
