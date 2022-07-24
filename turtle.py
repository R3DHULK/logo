#   The shapes those are exists
A = ['RECTANGLE', 'SQUARE', 'CIRCLE', 'TRIANGLE'] 
print (A)
B = input('Enter what you want to print :\n')
#  making the different types of shapes ----->

#  using turtle    (Creating turtle page)  --> 
import turtle

S = turtle.Turtle()
#  changing arrow & shape colour-->
S.color('red','yellow') 

#       ----- MAKING THE RECTANGLE-----
if (B == 'RECTANGLE') :
 def RECTANGLE() :
     S.begin_fill()
     S.forward(110)
     S.left(90)
     S.fd(110)
     S.left(90)
     S.fd(110)
     S.left(90)
     S.fd(110)
     S.left(90)
     S.end_fill()
     S.hideturtle()
 print(RECTANGLE()) 
 print('Done')
 turtle.mainloop()
#        ----- MAKING THE SQUARE -----
elif(B =='SQUARE') :
 def SQUARE() :
     S.begin_fill()
     S.fd(100)
     S.left(90)
     S.fd(100)
     S.left(90)
     S.fd(100)
     S.left(90)
     S.fd(100)
     S.left(90)
     S.end_fill()
     S.hideturtle()
 print(SQUARE())
 print('Done')
 turtle.mainloop()

#        ----- MAKING THE CIRCLE -----
elif B== 'CIRCLE' :
 def CIRCLE() :
 
     S.begin_fill()
     S.circle(70)
     S.end_fill()
     S.hideturtle()
 print(CIRCLE())
 print('Done')
 turtle.mainloop()

#        ----- MAKING THE TRIANGLE -----
elif B == 'TRIANGLE' :
 def TRIANGLE() :
     S.begin_fill()
     for T in range (3) :
         
         S.fd(150)
         S.left(120)
     S.end_fill()    
     S.hideturtle()   
 print(TRIANGLE() )   
 print('Done')   

 turtle.mainloop()
else :
    print("It doesn't exists")