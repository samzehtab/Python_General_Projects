
#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#S4 Book Exc03: Drawing Polygon

import turtle

def draw_poly(t, n, sz):
    '''
    Drawing a Polygon
    '''

    angle = 360 / n
    for _ in range(n):
        t.fd(sz)
        t.lt(angle)

### Driver Code ###

wn = turtle.Screen()
wn.bgcolor('LightGreen')
wn.title('Drawing Polygon')

tess = turtle.Turtle()
tess.color('HotPink', 'HotPink')
tess.pensize(3)

draw_poly(tess, 8, 50)

wn.mainloop()
