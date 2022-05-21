import turtle
from random import *
from turtle import *

penup()
goto(-140,140) #positioning the pen

for sp in range(15): #loop for creating the lines labelled with numbers
  speed(10)
 #setting the speed
  write(sp)
 #writing the int
  right(90)
 #setting right at 90 degrees
  forward(10)
 #forward at 10 units
  pendown()
 #ready to draw
  forward(150)
 #forward at 150 units
  penup()
 #not ready to draw
  backward(160)
 #back at 160 units
  left(90)
 #left set at 90 degrees
  forward(20)
 #forward at 20 units


hulk = Turtle() #inheriting the turtle
hulk.color('green') #setting the color to green for the first turtle
hulk.shape('turtle') #setting the shape to "turtle"
hulk.penup() #not ready to draw
hulk.goto(-160,100) #positioning the turtle
hulk.pendown() #ready todraw


sumalya = Turtle() #inheriting another turtle
sumalya.color('red') #setting the color og the turtle to red
sumalya.shape('turtle') #declaring the shape of the turtle to "turtle"
sumalya.penup() #not ready to draw
sumalya.goto(-160,80) #positioning
sumalya.pendown() #ready to draw

turtleVar = Turtle() #inheriting the last turtle
turtleVar.color('blue') #setting the color of the turtle as "blue"
turtleVar.shape('turtle') #declaring the shape of the turtle
turtleVar.penup() #not ready to draw
turtleVar.goto(-160,60) #positioning
turtleVar.pendown() #ready

for turn in range(100): #loop for the racew
  hulk.forward(randint(1,5)) #setting the speed randomly with the "random" module
  sumalya.forward(randint(1,5)) #setting the speed randomly with the "random" module
  turtleVar.forward(randint(1,5)) #setting the speed randomly with the "random" module
turtle.hideturtle()
turtle.done()