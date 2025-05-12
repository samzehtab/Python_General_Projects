# Mohammad Hossein Zehtab
# Advanced_Python_Wednesdays
# Project03: Point_and_Rectangle_Classes

def test(did_pass):
    """
    Print the result of a test.
    """
    if did_pass:
        print('True')
    else:
        print('Failed')


class Point:
    """
    A class for point objects with coordinates of x and y
    """
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"({self.x}, {self.y})"
        

class Rectangle:
    """
    A class for rectangle objects with corner coordinate, width and height.
    """
    
    def __init__(self, cornerpos, width, height):
        self.corner = cornerpos
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return(self.width + self.height) * 2
    
    def flip(self):
        self.width, self.height = self.height,self.width
        
    def contains(self, point1):
        if self.corner.x <= point1.x < self.width\
            and\
            self.corner.y <= point1.y < self.height:
            return True
        else:
            return False
        
    def __str__(self):
        return f"({self.corner}, {self.width}, {self.height})"
    

def test_suite():
    """
    Run the suite of tests for code in this module.
    """
    print("Question 1:")
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.area() == 50)
    
    print("\nQuestion 2:")
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.perimeter() == 30)
    
    print("\nQuestion 3:")
    r = Rectangle(Point(100, 50), 10, 5)
    test(r.width == 10 and r.height == 5)
    r.flip()
    test(r.width == 5 and r.height == 10)
    
    print("\nQuestion 4:")
    r = Rectangle(Point(0, 0), 10, 5)
    test(r.contains(Point(0, 0)))
    test(r.contains(Point(3, 3)))
    test(not r.contains(Point(3, 7)))
    test(not r.contains(Point(3, 5)))
    test(r.contains(Point(3, 4.99999)))
    test(not r.contains(Point(-3, -3)))

### Driver Code ###
test_suite()