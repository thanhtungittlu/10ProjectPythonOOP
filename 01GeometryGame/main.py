from random import randint
import turtle



class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
                and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return (self.point2.x - self.point1.x) * \
               (self.point2.y - self.point1.y)

class GUIRectangle(Rectangle):
    def draw(self,canvas):
        canvas.penup()
        canvas.goto(self.point1.x,self.point1.y)
        canvas.pendown()
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)
        canvas.left(90)
        canvas.forward(self.point2.x - self.point1.x)
        canvas.left(90)
        canvas.forward(self.point2.y - self.point1.y)

class GUIPoint(Point):
    def draw(self, canvas, size = 5, color = "red"):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.dot(size, color)

guiRectangle = GUIRectangle(Point(randint(0, 100), randint(0, 100)),Point(randint(200, 300), randint(200, 300)))
myTurtle = turtle.Turtle()

# Create rectangle object
# Print rectangle coordinates
print("Rectangle Coordinates: ",
      guiRectangle.point1.x, ",",
      guiRectangle.point1.y, "and",
      guiRectangle.point2.x, ",",
      guiRectangle.point2.y)

# Get point and area from user
user_point = GUIPoint(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(guiRectangle))
print("Your area was off by: ", guiRectangle.area() - user_area)

guiRectangle.draw(myTurtle)
user_point.draw(myTurtle)
turtle.done()
