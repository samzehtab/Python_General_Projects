#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S18 Book Ex01: Koch Snowflake

import turtle

def koch(t, order, size):
    '''
    Drawing a Koch Fractal
    '''
    if order == 0:
        t.fd(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order - 1, size/2)
            t.lt(angle)
    
### Driver Code ###

wn = turtle.Screen()
wn.bgcolor('LightGreen')
wn.title('Koch Snowflake')

tr = turtle.Turtle()
tr.speed(10)
tr.pensize(3)
tr.color('Blue', 'Blue')
tr.hideturtle()

for _ in range(3):
    koch(tr, 2, 100)
    tr.rt(120)

wn.mainloop()
