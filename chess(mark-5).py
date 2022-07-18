from turtle import *

import turtle 
   

scr = turtle.Screen()
turtle.title("Chess")
   

tur = turtle.Turtle()
   
# method to draw square
def draw():
   
  for i in range(4):
    tur.forward(30)
    tur.left(90)
   
  tur.forward(30)
   

if __name__ == "__main__" :
      
    scr.setup(600, 600)

    tur.speed(100)
       
    for i in range(8):
       

      tur.up()
       
      
      tur.setpos(0, 30 * i)
       

      tur.down()
       

      for j in range(8):
       
        # conditions for alternative color
        if (i + j)% 2 == 0:
          col ='black'
       
        else:
          col ='white'
       

        tur.fillcolor(col)
    
        tur.begin_fill()

        draw()
      
        tur.end_fill()
       

    tur.hideturtle()
tur.done()