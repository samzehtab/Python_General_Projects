
#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S18 Book Ex02a: Cesaro Torn Line

import turtle

def cesaro(t, order, size):
    '''
    Drawing a Cesaro Fractal
    '''
    if order == 0:
        t.fd(size)
    else:
        for angle in [85, -170, 85, 0]:
            cesaro(t, order - 1, size/2)
            t.rt(angle)
    
### Driver Code ###

wn = turtle.Screen()
wn.bgcolor('LightGreen')
wn.title('Koch Snowflake')

tr = turtle.Turtle()
tr.speed(10)
tr.pensize(1)
tr.color('Blue', 'Blue')
tr.hideturtle()

cesaro(tr, 3, 200)

wn.mainloop()

