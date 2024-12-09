# In the name of God
# Mohammad Hossein Zehtab
# python-evens-17
# Project 05: Point Class

class Point:
    '''
    Point class represents and manipulates x & y Coordinates.
    '''

    def __init__(self, x=0, y=0):
        '''
        Creates a new point at x & y
        '''
        self.x = x
        self.y = y


    def euclidean_distance_from_origin(self):
        '''
        Euclidean Distance between myself and the origin.
        '''
        addsq = self.x ** 2 + self.y ** 2
        distfromorigin = addsq ** 0.5
        return distfromorigin


    def euclidean_distance(self, target):
        '''
        Euclidean Distance between myself and a target.
        '''
        addsq = (target.x - self.x) ** 2 + (target.y - self.y) ** 2
        dist = addsq ** 0.5
        return dist


    def manhattan_distance(self, target):
        '''
        Manhattan Distance between myself and a target.
        '''
        sub1 = target.x - self.x
        sub2 = target.y - self.y
        dist = abs(sub1) + abs(sub2)
        return dist
    
    
    def halfway(self, target):
        '''
        Mid point between myself and a target.
        '''
        pointx = (target.x + self.x) / 2
        pointy = (target.y + self.y) / 2
        point = (pointx, pointy)
        return point
    
    
    def __str__(self):
       '''
       Shows the value of a point object.
       ''' 
       return f'({self.x}, {self.y})'
    
    
### Instantiations ###

p = Point()
p.x = 6
p.y = 8
print('p =', p)

q = Point()
q.x = 3
q.y = 7
print('q =', q)

# Euclidean distance from origin
edfo = p.euclidean_distance_from_origin()
print(f'\nEuclidean Distance between {p} and the origin is {edfo:.2f}')

# Euclidean distance between two points
ed = p.euclidean_distance(q)
print(f'\nEuclidean Distance between {p} and {q} is {ed:.2f}')

# Manhattan distance between two points
md = p.manhattan_distance(q)
print(f'\nManhattan Distance between {p} and {q} is {md:.2f}')

# Halfway between two points
hp = p.halfway(q)
print(f'\nHalfway Point between {p} and {q} is {hp}')