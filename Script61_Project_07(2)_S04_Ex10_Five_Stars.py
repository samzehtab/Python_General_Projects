# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 07 Part2 S04 Exc10: Five Stars

import turtle

def draw_star(tur, size: float, angle: float):
    '''
    Draw a Star
    '''
    for _ in range(5):
        tur.fd(size)
        tur.rt(angle)

### Driver Code ###

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tr=turtle.Turtle()
tr.pensize(3)
tr.color('hotpink', 'hotpink')
tr.speed(0)

tr.up()
tr.goto(-225, 50)
tr.down()

angles = [0, 144, 288, 72, -144]
for angle in angles:
    tr.up()
    tr.fd(350)
    tr.lt(angle)
    tr.down()
    draw_star(tr, 100, 144)
    tr.rt(angle + 144)

wn.mainloop()

