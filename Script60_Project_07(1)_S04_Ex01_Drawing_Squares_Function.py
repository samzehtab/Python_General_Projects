#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#Project 07 Part1 S04 Exc01: Drawing Squares Function

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
        
    tur.up()
    tur.fd(size * 2)
    tur.down()

### Driver Code ###

for _ in range(5):
    draw_square(tr, 20)
