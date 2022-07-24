import turtle
t = turtle.Turtle()

#SQUARE
side = int(input("Length of side: "))
for i in range(4):
   t.forward(side)
   t.left(90)

#RECTANGLE
side_a = int(input("Length of side a: "))
side_b = int(input("Length of side b: "))
t.forward(side_a)
t.left(90)
t.forward(side_b)
t.left(90)
t.forward(side_a)
t.left(90)
t.forward(side_b)
t.left(90)

#CIRCLE
radius = int(input("Radius of circle: "))
t.circle(radius)

#HEXAGON
for i in range(6):
   t.forward(side)
   t.left(300)