#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#Lec 11: Olympic Flag with Distance

import turtle

class Point:
    '''
    Point class represents and manipulates x & y Coordinates.
    '''

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, target):
        '''
        Distance between myself and a target.
        '''
        addsq = (target.x - self.x) ** 2 + (target.y - self.y) ** 2
        dist = addsq ** 0.5
        return dist


def drawing_olympic(radius):
    '''
    Drawing Olympic Flag
    '''

    i = 0
    d = radius * 2

    wn = turtle.Screen()
    wn.title('Olympic Flag')

    tr = turtle.Turtle()
    tr.speed(15)
    tr.pensize(radius / 6)
    tr_color1 = 'blue', 'black', 'red'
    tr_color2 = 'green', 'orange'
    tr.shape('blank')

    tr.up()
    tr.bk(d + d / 8)
    tr.down()
    for color in tr_color1:
        tr.pencolor(color)
        tr.circle(radius)
        tr.up()
        tr.goto(i, 0)
        tr.down()
        i += d + d / 8

    tr.up()
    tr.goto(radius + d / 16, -(radius + radius / 8))
    tr.down()
    for color in tr_color2:
        tr.pencolor(color)
        tr.circle(radius)
        tr.up()
        tr.bk(d + d / 8)
        tr.down()

    wn.mainloop()

### Driver Code ###

p = Point(10, 10)
q = Point(70, 90)

drawing_olympic(p.distance(q))
