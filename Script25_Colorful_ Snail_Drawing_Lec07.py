
#In the name of God
#Mohammad Hossein Zehtab
#python-evens-17
#Colorful Snail Drawing

import turtle

wn = turtle.Screen()
wn.title('Colorful Snail Drawing')

tr = turtle.Turtle()
tr.up()

color = ['red', 'green', 'blue', 'cyan']
d = 10
for _ in range(8):
    for c in color:
        tr.color(c, c)
        tr.stamp()
        tr.up()
        tr.rt(25)
        tr.fd(d)
        d += 3
tr.shape('blank')
wn.mainloop()
