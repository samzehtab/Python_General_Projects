#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S18 Book Ex02b: Cesaro Squares

import turtle

def cesarosq(t, order, size, angle):
    '''
    Drawing a Cesaro Square Fractal
    '''
    ang = [90 - angle / 2,
           -(180 - angle),
           90 - angle / 2,
           0]
    if order == 0:
        t.fd(size)
    else:
        for a in ang:
            cesarosq(t, order - 1, size/2, angle)
            t.rt(a)
    
### Driver Code ###

wn = turtle.Screen()
wn.bgcolor('LightGreen')
wn.title('Koch Snowflake')

tr = turtle.Turtle()
tr.speed(0)
tr.pensize(1)
tr.color('Blue', 'Blue')
tr.hideturtle()

for _ in range(4):
    cesarosq(tr, 3, 150, 10)
    tr.rt(90)

wn.mainloop()
