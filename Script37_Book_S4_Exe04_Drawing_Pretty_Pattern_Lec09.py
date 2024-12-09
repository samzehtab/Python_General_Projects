
#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S4 Book Exc04: Drawing Pretty Pattern

import turtle

def draw_square(tur, size: float):
    '''
    Draw a Square
    '''

    for _ in range(4):
        tur.fd(size)
        tur.lt(90)
        
### Driver Code ###

wn = turtle.Screen()
wn.bgcolor('LightGreen')

tr=turtle.Turtle()
tr.speed(10)
tr.pensize(3)
tr.color('Blue', 'Blue')

for _ in range(20):
    draw_square(tr, 100)
    tr.lt(18)
    
wn.mainloop()
