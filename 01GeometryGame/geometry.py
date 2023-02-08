class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def fallPointInRectangle(self, rectangle):
        if  rectangle.lowLeft.x < self.x < rectangle.upRight.y \
        and rectangle.lowLeft.y < self.y < rectangle.upRight.y:
            return True
        else:
            return False
        

    def distanceFromPoint(self, point):
        return ((self.x - point.x)**2 + (self.y - point.y)**2) ** 0.5

class Rectangle:
    def __init__(self, lowLeft, upRight):
        self.lowLeft = lowLeft
        self.upRight = upRight

    def getArea(self):
        return (self.upRight.x - self.lowLeft.x) * (self.upRight.y - self.lowLeft.y)

point1 = Point(7,8)
point2 = Point(4,5)
rectangle = Rectangle( Point(5,6) , Point(9,10))
print( point1.fallPointInRectangle(rectangle) )
print(point1.distanceFromPoint(point2))
print( rectangle.getArea() )


   