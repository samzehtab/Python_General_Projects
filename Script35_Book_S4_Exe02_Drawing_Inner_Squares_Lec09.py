#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S4 Book Exc02: Drawing Inner Squares

import turtle

wn = turtle.Screen()
wn.bgcolor('lightgreen')

tr=turtle.Turtle()
tr.pensize(3)
tr.color('hotpink', 'hotpink')

def draw_square(tur, size: float):
    '''
    Draw a Square
    '''

    for _ in range(4):
        tur.fd(size)
        tur.lt(90)

### Driver Code ###

for i in range(5):
    draw_square(tr, 20 + i * 20)
    tr.up()
    tr.goto(-10 * (i + 1), -10 * (i + 1))
    tr.down()
